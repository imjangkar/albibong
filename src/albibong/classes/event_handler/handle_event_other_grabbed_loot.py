from albibong.classes.character import Character
from albibong.classes.world_data import WorldData
from albibong.threads.websocket_server import send_event


def handle_event_other_grabbed_loot(world_data: WorldData, parameters):

    # update char data
    if 2 in parameters and parameters[2] in world_data.characters:
        char: Character = world_data.characters[parameters[2]]
        char.update_loot(parameters)
        event = {
            "type": "update_silver",
            "payload": {
                "username": char.username,
                "silver_gained": char.silver_gained,
            },
        }
        send_event(event)

    # update dungeon data
    if world_data.current_dungeon and parameters[2] == world_data.me.username:
        world_data.current_dungeon.update_loot(parameters)
