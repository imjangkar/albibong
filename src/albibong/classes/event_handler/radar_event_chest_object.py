from albibong.classes.world_data import WorldData


def radar_event_new_loot_chest(world_data: WorldData, parameters):
    id = parameters[0]
    location = parameters[1]
    name = parameters[3]
    name2 = parameters[4]

    world_data.radar.add_cheast(id, location, name, name2, parameters)    

def radar_event_new_treasure_chest(world_data: WorldData, parameters):
    print("radar_event_new_treasure_chest")
    print(parameters)
    
def radar_event_new_match_loot_chest_object(world_data: WorldData, parameters):
    print("radar_event_new_match_loot_chest_object")
    print(parameters)

