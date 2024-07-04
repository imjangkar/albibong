from albibong.classes.event_handler.world_data_utils import WorldDataUtils
from albibong.classes.location import Location
from albibong.classes.world_data import WorldData
from albibong.threads.websocket_server import send_event


def handle_operation_change_cluster(world_data: WorldData, parameters):
    world_data.change_equipment_log = {}

    if 1 in parameters:
        check_map = Location.get_location_from_code(parameters[1])
        map_type_splitted = set(check_map.type.split("_"))
        WorldDataUtils.set_dungeon_status(world_data, check_map, map_type_splitted)

        if "ISLAND" in map_type_splitted or "HIDEOUT" in map_type_splitted:
            check_map.name = f"{parameters[2]}'s {check_map.name}"
            world_data.current_map = check_map

    elif 0 in parameters:
        check_map = Location.get_location_from_code(parameters[0])
        map_type_splitted = set(check_map.type.split("_"))
        is_dungeon = WorldDataUtils.set_dungeon_status(
            world_data, check_map, map_type_splitted
        )
        if is_dungeon == False:
            world_data.current_map = Location.get_location_from_code(parameters[0])

    ws_update_location(world_data)


def ws_update_location(world_data: WorldData):
    event = {
        "type": "update_location",
        "payload": {
            "map": world_data.current_map.name if world_data.current_map else "None",
            "dungeon": (
                world_data.current_dungeon.name
                if world_data.current_dungeon
                else "None"
            ),
        },
    }
    send_event(event)
