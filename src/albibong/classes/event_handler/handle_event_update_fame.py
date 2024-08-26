from albibong.classes.world_data import WorldData
from albibong.threads.websocket_server import send_event


def handle_event_update_fame(world_data: WorldData, parameters):
    world_data.me.update_fame(parameters)
    event = {
        "type": "update_fame",
        "payload": {
            "username": world_data.me.username,
            "fame_gained": world_data.me.fame_gained,
        },
    }
    send_event(event)
    if world_data.current_dungeon:
        world_data.current_dungeon.update_fame(parameters)
