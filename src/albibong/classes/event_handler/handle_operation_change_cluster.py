from albibong.classes.event_handler.world_data_utils import WorldDataUtils
from albibong.classes.location import Island, Location
from albibong.classes.world_data import WorldData
from albibong.threads.websocket_server import send_event


def handle_operation_change_cluster(world_data: WorldData, parameters):
    world_data.change_equipment_log = {}

    if type(world_data.current_map).__name__ == "Island":
        WorldDataUtils.set_island_status(
            current_island=world_data.current_map, parameters=parameters
        )

    if 1 in parameters:
        check_map = Location.get_location_from_code(parameters[1])
        map_type_splitted = set(check_map.type.split(" "))
        WorldDataUtils.set_dungeon_status(world_data, check_map, map_type_splitted)

        if "ISLAND" in map_type_splitted:
            island = Island.get_island_from_code(parameters[1])
            island.name = f"{parameters[2]}'s {island.name}"
            world_data.current_map = island
        elif "HIDEOUT" in map_type_splitted:
            hideout = Location.get_location_from_code(parameters[1])
            hideout.name = f"{parameters[2]}'s {hideout.name}"
            world_data.current_map = hideout

    elif 0 in parameters:
        check_map = Location.get_location_from_code(parameters[0])
        map_type_splitted = set(check_map.type.split(" "))
        is_dungeon = WorldDataUtils.set_dungeon_status(
            world_data, check_map, map_type_splitted
        )
        if is_dungeon == False:
            world_data.current_map = Location.get_location_from_code(parameters[0])

    WorldDataUtils.ws_update_location(world_data)
