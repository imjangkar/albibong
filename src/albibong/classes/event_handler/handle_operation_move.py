from albibong.classes.world_data import WorldData


def handle_operation_move(world_data: WorldData, parameters):
    if not world_data.me:
        return
    
    if 3 in parameters:
        world_data.radar.update_position(parameters[3][0], parameters[3][1])

    world_data.me.update_coords(parameters)


