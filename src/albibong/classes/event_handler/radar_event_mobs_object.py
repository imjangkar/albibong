from albibong.classes.world_data import WorldData

def radar_event_mob_change_state(world_data: WorldData, parameters):
    id = parameters[0]
    enchant = parameters[1]

    world_data.radar.updateMobEnchant(id, enchant)

def radar_event_new_mob(world_data: WorldData, parameters):
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

