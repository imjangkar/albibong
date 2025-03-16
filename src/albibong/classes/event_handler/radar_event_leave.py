from albibong.classes.world_data import WorldData

def radar_event_leave(world_data: WorldData, parameters):
    id = parameters[0]
    world_data.radar.handle_event_leave(id)
