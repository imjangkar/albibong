from albibong.classes.world_data import WorldData
from albibong.resources.Offset import Offsets

def radar_event_leave(world_data: WorldData, parameters):
    LEAVE = [0],
    LEAVE = LEAVE[0]
    
    id = parameters[Offsets.LEAVE[0]]
    world_data.radar.handle_event_leave(id)
    