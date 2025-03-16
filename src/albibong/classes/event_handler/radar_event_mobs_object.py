from albibong.classes.world_data import WorldData



def radar_event_new_mob(world_data: WorldData, parameters):
    id = parameters[0]
    type_id = parameters[1]
    location = parameters[7]
    try:
        exp = float(parameters[13])
    except Exception:
        exp = 0
    
    name = None
    try:
        name = parameters[32]
    except Exception:
        name = None

    enchant = None
    try:
        enchant = parameters[33]
    except Exception:
        enchant = None

    if name is None:
        try:
            name = parameters[31]
        except Exception:
            name = None

    rarity = 1
    
    try:
        rarity = int(parameters[19])
    except Exception:
        rarity = 1

    if name is not None:
        world_data.radar.add_mist(id, location, name, enchant, parameters)
    else:
        world_data.radar.add_mob(id, type_id, location, exp, rarity, parameters)

