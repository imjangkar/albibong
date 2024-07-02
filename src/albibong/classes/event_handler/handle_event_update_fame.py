from albibong.classes.world_data import WorldData


def handle_event_update_fame(world_data: WorldData, parameters):
    world_data.me.update_fame(parameters)
    if world_data.current_dungeon:
        world_data.current_dungeon.update_fame(parameters)
