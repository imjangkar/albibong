from collections import deque
import json
import os

from albibong.classes.character import Character
from albibong.classes.dungeon import Dungeon
from albibong.classes.location import Location
from albibong.classes.utils import Utils
from albibong.classes.world_data import WorldData
from albibong.threads.websocket_server import send_event

FILENAME = os.path.join(os.path.expanduser("~"), "Albibong/list_dungeon.json")
os.makedirs(os.path.dirname(FILENAME), exist_ok=True)


class WorldDataUtils:

    def end_current_dungeon(world_data: WorldData):
        if world_data.current_dungeon:
            list_dungeon = deque()

            try:
                with open(FILENAME) as json_file:
                    list_dungeon = deque(json.load(json_file))
            except:
                pass

            world_data.current_dungeon.get_elapsed_time()
            list_dungeon.appendleft(Dungeon.serialize(world_data.current_dungeon))

            with open(FILENAME, "w") as json_file:
                json.dump(list(list_dungeon), json_file)

            WorldDataUtils.ws_update_dungeon(list(list_dungeon))

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
            new_dungeon = Dungeon(type, name)
            world_data.current_dungeon = new_dungeon

    @staticmethod
    def set_dungeon_status(
        world_data: WorldData, check_map: Location, map_type_splitted: set
    ):
        if "EXPEDITION" in map_type_splitted or "DUNGEON" in map_type_splitted:
            WorldDataUtils.start_current_dungeon(
                world_data, type=check_map.type, name=check_map.name
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

        WorldDataUtils.ws_update_damage_heal(world_data)

    def ws_update_damage_heal(world_data: WorldData):
        event = {
            "type": "update_dps",
            "payload": {"party_members": world_data.serialize_party_members()},
        }
        send_event(event)
