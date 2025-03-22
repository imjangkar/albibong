from albibong.classes.world_data import WorldData

def radar_event_key_sync(world_data: WorldData, parameters):
    # TODO handle KEY_SYNC
    # print("@@@@@@@@@@@@@@@@ radar_event_key_sync", parameters)
    world_data.radar.handle_event_key_sync(parameters[0])
