from albibong.classes.world_data import WorldData
from albibong.threads.websocket_server import send_event


def handle_event_character_equipment_changed(world_data: WorldData, parameters):
    if 2 in parameters:
        if parameters[0] in world_data.char_id_to_username:
            if world_data.char_id_to_username[parameters[0]] != "not initialized":
                char = world_data.characters[
                    world_data.char_id_to_username[parameters[0]]
                ]
                if char.username in world_data.party_members:
                    char.update_equipment(parameters[2])
                    ws_update_character_equipment(world_data)
        else:
            world_data.change_equipment_log[parameters[0]] = parameters[2]


def ws_update_character_equipment(world_data: WorldData):
    event = {
        "type": "update_dps",
        "payload": {"party_members": world_data.serialize_party_members()},
    }
    send_event(event)
