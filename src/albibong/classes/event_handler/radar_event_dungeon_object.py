from albibong.classes.world_data import WorldData

def radar_event_random_dungeon_position_info(world_data: WorldData, parameters):
    print("radar_event_new_simple_harvestable_object")
    print(parameters)

def radar_event_new_random_dungeon_exists(world_data: WorldData, parameters):
    id = parameters[0]
    location = parameters[1]
    name = parameters[3]
    enchat = parameters[8]

    world_data.radar.add_dungeon(id, location, name, enchat, parameters)
