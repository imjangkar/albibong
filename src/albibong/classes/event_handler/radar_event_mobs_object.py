from albibong.classes.world_data import WorldData
from albibong.resources.Offset import Offsets

def radar_event_mob_change_state(world_data: WorldData, parameters):
    id = parameters[Offsets.MOB_CHANGE_STATE[0]]
    enchant = parameters[Offsets.MOB_CHANGE_STATE[1]]

    world_data.radar.updateMobEnchant(id, enchant)

def radar_event_new_mob(world_data: WorldData, parameters):
    NEW_MOB_EVENT = [0, 1, 8, 13, 14, 33],

    id = parameters[Offsets.NEW_MOB_EVENT[0]]
    type_id = parameters[Offsets.NEW_MOB_EVENT[1]]
    location = parameters[Offsets.NEW_MOB_EVENT[2]]
    mob_current_health = parameters[Offsets.NEW_MOB_EVENT[3]] if Offsets.NEW_MOB_EVENT[3] in parameters else parameters[Offsets.NEW_MOB_EVENT[4]]
    mob_max_health = parameters[Offsets.NEW_MOB_EVENT[4]]
    enchant = parameters[Offsets.NEW_MOB_EVENT[5]] if Offsets.NEW_MOB_EVENT[5] in parameters else 0

    world_data.radar.add_new_mob(id, type_id, location, mob_current_health, mob_max_health, enchant)
    

def radar_event_new_mob_old(world_data: WorldData, parameters):
    NEW_MOB_EVENT = [0, 1, 8, 13, 14, 33],

    id = parameters[0]
    type_id = parameters[1]
    location = parameters[7]
    
    name = None
    enchant = None

    try:
        name = parameters[32]
    except Exception:
        name = None

    if name is None:
        try:
            name = parameters[31]
        except Exception:
            name = None

    try:
        enchant = parameters[33]
    except Exception:
        enchant = None

    
    if name is not None:
        
        world_data.radar.add_mist(id, location, name, enchant, parameters)
    else:
        world_data.radar.add_mob(id, type_id, location, enchant, parameters)

