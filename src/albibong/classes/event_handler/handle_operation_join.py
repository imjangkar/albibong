from albibong.classes.dungeon import Dungeon
from albibong.classes.event_handler.world_data_utils import WorldDataUtils
from albibong.classes.location import Location
from albibong.classes.utils import Utils
from albibong.classes.world_data import WorldData
from albibong.threads.websocket_server import send_event


def handle_operation_join(world_data: WorldData, parameters):
    # set my character
    WorldDataUtils.convert_id_to_name(
        world_data, old_id=world_data.me.id, new_id=parameters[0], char=world_data.me
    )
    world_data.me.uuid = Utils.convert_int_arr_to_uuid(parameters[1])
    world_data.me.username = parameters[2]
    world_data.me.guild = parameters[57] if 57 in parameters else ""
    world_data.me.alliance = parameters[77] if 77 in parameters else ""
    if world_data.me.id in world_data.change_equipment_log:
        world_data.me.update_equipment(
            world_data.change_equipment_log[world_data.me.id]
        )

    # put self in characters list
    world_data.characters[world_data.me.username] = world_data.me
    world_data.char_uuid_to_username[world_data.me.uuid] = world_data.me.username

    # put self in party
    world_data.party_members.add(world_data.me.username)

    # set map my character is currently in
    if parameters[8][0] == "@":
        area = parameters[8].split("@")
        if area[1] == "RANDOMDUNGEON":
            check_map = Location.get_location_from_code(area[1])
            WorldDataUtils.start_current_dungeon(
                world_data, type=check_map.type, name=check_map.name
            )

    ws_init_character(world_data)
    ws_update_location(world_data)
    ws_update_dps(world_data)


def ws_init_character(world_data: WorldData):
    event = {
        "type": "init_character",
        "payload": {
            "username": world_data.me.username,
            "fame": world_data.me.fame_gained,
            "re_spec": world_data.me.re_spec_gained,
            "silver": world_data.me.silver_gained,
            "weapon": world_data.me.equipment[0].image,
        },
    }
    send_event(event)


def ws_update_location(world_data: WorldData):
    event = {
        "type": "update_location",
        "payload": {
            "map": world_data.current_map.name if world_data.current_map else "None",
            "dungeon": (
                Dungeon.serialize(world_data.current_dungeon)
                if world_data.current_dungeon
                else None
            ),
        },
    }
    send_event(event)


def ws_update_dps(world_data: WorldData):
    event = {
        "type": "update_dps",
        "payload": {"party_members": world_data.serialize_party_members()},
    }
    send_event(event)
