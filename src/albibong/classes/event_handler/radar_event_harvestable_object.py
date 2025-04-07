from albibong.classes.world_data import WorldData
from albibong.resources.Offset import Offsets

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
    id = parameters[Offsets.NEW_HARVESTABLE_OBJECT[0]]
    type = parameters[Offsets.NEW_HARVESTABLE_OBJECT[1]]
    tier = parameters[Offsets.NEW_HARVESTABLE_OBJECT[2]]
    location = parameters[Offsets.NEW_HARVESTABLE_OBJECT[3]]
    size = parameters[Offsets.NEW_HARVESTABLE_OBJECT[4]] if Offsets.NEW_HARVESTABLE_OBJECT[4] in parameters else 0
    enchant = parameters[Offsets.NEW_HARVESTABLE_OBJECT[5]] if Offsets.NEW_HARVESTABLE_OBJECT[5] in parameters else 0

    world_data.radar.add_harvestable(id, type, tier, location[0], location[1], enchant, size)

def radar_event_harvest_change_state(world_data: WorldData, parameters):
    id = parameters[Offsets.HARVESTABLE_CHANGE_STATE[0]]
    size = parameters[Offsets.HARVESTABLE_CHANGE_STATE[1]] if Offsets.HARVESTABLE_CHANGE_STATE[1] in parameters else 0
    enchant = parameters[Offsets.HARVESTABLE_CHANGE_STATE[2]] if Offsets.HARVESTABLE_CHANGE_STATE[2] in parameters else 0

    world_data.radar.update_harvestable(id, size, enchant)

