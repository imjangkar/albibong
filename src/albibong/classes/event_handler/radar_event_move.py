from albibong.classes.world_data import WorldData

def radar_event_move(world_data: WorldData, parameters):
    id = parameters[0]
    posX = parameters[4]
    posY = parameters[5]
    world_data.radar.handle_event_move(id, posX, posY)
