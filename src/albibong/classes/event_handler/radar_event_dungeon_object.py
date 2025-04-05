from albibong.classes.world_data import WorldData
from albibong.resources.Offset import Offsets


def radar_event_random_dungeon_position_info(world_data: WorldData, parameters):
    print("radar_event_new_simple_harvestable_object")
    print(parameters)

def radar_event_new_random_dungeon_exists(world_data: WorldData, parameters):
    id = parameters[Offsets.NEW_DUNGEON_EXIT[0]]
    location = parameters[Offsets.NEW_DUNGEON_EXIT[1]]
    name = parameters[Offsets.NEW_DUNGEON_EXIT[2]]
    enchat = parameters[Offsets.NEW_DUNGEON_EXIT[3]]

    world_data.radar.add_dungeon(id, location, name, enchat, parameters)
