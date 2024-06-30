from albibong.classes.world_data import WorldData


def handle_operation_move(world_data: WorldData, parameters):
    if not world_data.me:
        return

    world_data.me.update_coords(parameters)
