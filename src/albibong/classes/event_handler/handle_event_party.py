from uuid import UUID
from albibong.classes.world_data import WorldData
from albibong.threads.websocket_server import send_event


def handle_event_party_joined(world_data: WorldData, parameters):
    world_data.party_members = set(parameters[5])
    ws_update_party_member(world_data)


def handle_event_party_disbanded(world_data: WorldData, parameters):
    world_data.party_members = {world_data.me.username}
    ws_update_party_member(world_data)


def handle_event_party_player_joined(world_data: WorldData, parameters):
    world_data.party_members.add(parameters[2])
    ws_update_party_member(world_data)


def handle_event_party_player_left(world_data: WorldData, parameters):
    uuid = UUID(bytes=bytes(parameters[1]))

    if uuid in world_data.char_uuid_to_username:
        name = world_data.char_uuid_to_username[uuid]

        # self out party
        if name == world_data.me.username:
            world_data.party_members = {world_data.me.username}
            ws_update_party_member(world_data)


def ws_update_party_member(world_data: WorldData):
    event = {
        "type": "update_dps",
        "payload": {"party_members": world_data.serialize_party_members()},
    }
    send_event(event)
