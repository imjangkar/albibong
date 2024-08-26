from albibong.classes.world_data import WorldData
from albibong.threads.websocket_server import send_event


def handle_event_might_and_favor_received_event(world_data: WorldData, parameters):
    world_data.me.update_might_and_favor(parameters)
    event = {
        "type": "update_might_and_favor",
        "payload": {
            "username": world_data.me.username,
            "favor_gained": world_data.me.favor_gained,
            "might_gained": world_data.me.might_gained,
        },
    }
    send_event(event)

    if world_data.current_dungeon:
        world_data.current_dungeon.update_might_and_favor(parameters)
