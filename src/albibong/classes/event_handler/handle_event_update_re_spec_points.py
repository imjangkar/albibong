from albibong.classes.world_data import WorldData
from albibong.threads.websocket_server import send_event


def handle_event_update_re_spec_points(world_data: WorldData, parameters):

    # update char data
    world_data.me.update_re_spec(parameters)
    event = {
        "type": "update_re_spec",
        "payload": {
            "username": world_data.me.username,
            "re_spec_gained": world_data.me.re_spec_gained,
        },
    }
    send_event(event)

    # update dungeon data
    if world_data.current_dungeon:
        world_data.current_dungeon.update_re_spec(parameters)
