from albibong.classes.world_data import WorldData

def radar_event_new_simple_harvestable_object(world_data: WorldData, parameters):
    if len(parameters[0]) == 0:
        return
    
    a0 = parameters[0]
    a1 = parameters[1]
    a2 = parameters[2]
    a3 = parameters[3]
    a4 = parameters[4]

    for i in range(len(parameters[0])):
        id = a0[i]
        type = a1[i]
        tier = a2[i]
        posX = a3[i * 2]
        posY = a3[i * 2 + 1]
        count = a4[i]

        if tier < 2:
            continue
        world_data.radar.add_harvestable(id, type, tier, posX, posY, 0, count)

def radar_event_new_harvestable_object(world_data: WorldData, parameters):
    id = parameters[0]
    type = parameters[5]
    tier = parameters[7]
    location = parameters[8]

    enchant = parameters[11] if 11 in parameters else 0
    size = parameters[10] if 10 in parameters else 0

    world_data.radar.add_harvestable(id, type, tier, location[0], location[1], enchant, size)

def radar_event_harvest_finished(world_data: WorldData, parameters):
    id = parameters[0]
    size = parameters[1] if 1 in parameters else 0

    world_data.radar.update_harvestable(id, size)