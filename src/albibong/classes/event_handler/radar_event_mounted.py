from albibong.classes.world_data import WorldData
from albibong.resources.Offset import Offsets

def radar_event_mounted(world_data: WorldData, parameters):
    id_key = Offsets.MOUNTED[0]
    is_mounted_key = Offsets.MOUNTED[1]

    id = parameters[id_key]
    is_mounted = True if is_mounted_key in parameters else False
    world_data.radar.player_mounted(id, is_mounted)