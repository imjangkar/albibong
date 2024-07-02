from albibong.classes.world_data import WorldData


def handle_event_update_re_spec_points(world_data: WorldData, parameters):

    # update char data
    world_data.me.update_re_spec(parameters)

    # update dungeon data
    if world_data.current_dungeon:
        world_data.current_dungeon.update_re_spec(parameters)
