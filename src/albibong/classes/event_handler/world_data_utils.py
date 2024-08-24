from albibong.classes.character import Character
from albibong.classes.dungeon import Dungeon
from albibong.classes.location import Island, Location
from albibong.classes.world_data import WorldData
from albibong.threads.websocket_server import send_event


class WorldDataUtils:

    def save_current_island(current_map: Island):
        current_map.save(force_insert=True)
        WorldDataUtils.ws_update_total_harvest_by_date(
            Island.get_total_harvest_by_date()
        )
        WorldDataUtils.ws_update_island(Island.get_all_island())

    def set_island_status(current_island: Island, parameters):
        check_map = (
            Location.get_location_from_code(parameters[1])
            if 1 in parameters
            else Location.get_location_from_code(parameters[0])
        )
        check_map_name = (
            f"{parameters[2]}'s {check_map.name}" if 2 in parameters else check_map.name
        )
        if current_island.name != check_map_name:
            if current_island.crops != {} or current_island.animals != {}:
                WorldDataUtils.save_current_island(current_island)

    def ws_update_total_harvest_by_date(payload):
        event = {
            "type": "update_total_harvest_by_date",
            "payload": payload,
        }
        send_event(event)

    def ws_update_island(list_island: list):
        event = {
            "type": "update_island",
            "payload": {"list_island": list_island},
        }
        send_event(event)

    def end_current_dungeon(world_data: WorldData):
        if world_data.current_dungeon:
            world_data.current_dungeon.set_end_time()
            world_data.current_dungeon.update_meter(
                world_data.serialize_party_members()
            )
            world_data.current_dungeon.save(force_insert=True)
            WorldDataUtils.ws_update_dungeon(Dungeon.get_all_dungeon())
            world_data.current_dungeon = None

    def ws_update_dungeon(list_dungeon: list):
        event = {
            "type": "update_dungeon",
            "payload": {"list_dungeon": list_dungeon},
        }
        send_event(event)

    @staticmethod
    def start_current_dungeon(world_data: WorldData, type: str, name: str):
        if world_data.current_dungeon == None:
            new_dungeon = Dungeon(type=type, name=name)
            world_data.current_dungeon = new_dungeon

    @staticmethod
    def set_dungeon_status(
        world_data: WorldData, check_map: Location, map_type_splitted: set
    ):
        if "EXPEDITION" in map_type_splitted or "HELLGATE" in map_type_splitted:
            WorldDataUtils.start_current_dungeon(
                world_data, type=check_map.type, name=check_map.name
            )
        elif "DUNGEON" in map_type_splitted:
            WorldDataUtils.start_current_dungeon(
                world_data,
                type=check_map.type,
                name=(
                    f"{check_map.name} at {world_data.current_map.name}"
                    if world_data.current_map
                    else check_map.name
                ),
            )
        elif (
            "EXPEDITION" not in map_type_splitted or "DUNGEON" not in map_type_splitted
        ):
            WorldDataUtils.end_current_dungeon(world_data)
            return False

    @staticmethod
    def convert_id_to_name(world_data: WorldData, old_id, new_id, char: Character):
        if old_id in world_data.char_id_to_username:
            world_data.char_id_to_username.pop(old_id)  # delete old relative id
        char.id = new_id
        world_data.char_id_to_username[char.id] = char.username  # add new relative id

    @staticmethod
    def update_damage_or_heal(world_data: WorldData, target, inflictor, nominal):

        if inflictor not in world_data.char_id_to_username:
            # character not initialized yet
            return

        username = world_data.char_id_to_username[inflictor]

        if username == "not initialized":
            # self not initialized
            return

        char: Character = world_data.characters[username]

        if nominal < 0:
            if target == inflictor:
                # suicide
                return
            char.update_damage_dealt(abs(nominal))
        else:
            char.update_heal_dealt(nominal)

        WorldDataUtils.ws_update_damage_meter(world_data)

    def ws_update_damage_meter(world_data: WorldData):
        event = {
            "type": "update_damage_meter",
            "payload": {"party_members": world_data.serialize_party_members()},
        }
        send_event(event)

    def ws_update_location(world_data: WorldData):
        event = {
            "type": "update_location",
            "payload": {
                "map": (
                    world_data.current_map.name if world_data.current_map else "None"
                ),
                "dungeon": (
                    world_data.current_dungeon.name
                    if world_data.current_dungeon
                    else "None"
                ),
            },
        }
        send_event(event)
