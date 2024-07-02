from albibong.classes.character import Character
from albibong.classes.world_data import WorldData
from albibong.threads.websocket_server import send_event


def handle_event_health_update(world_data: WorldData, parameters):

    if world_data.is_dps_meter_running == False:
        return

    if 0 not in parameters or 6 not in parameters or 2 not in parameters:
        return

    nominal = parameters[2]
    target = parameters[0]
    inflictor = parameters[6]

    update_damage_or_heal(world_data, target, inflictor, nominal)


def handle_event_health_updates(world_data: WorldData, parameters):

    if world_data.is_dps_meter_running == False:
        return

    if 0 not in parameters or 6 not in parameters or 2 not in parameters:
        return

    for i in range(len(parameters[2])):
        nominal = parameters[2][i]
        target = parameters[0]
        inflictor = parameters[6][i]

        update_damage_or_heal(world_data, target, inflictor, nominal)


def update_damage_or_heal(world_data: WorldData, target, inflictor, nominal):

    if inflictor not in world_data.char_id_to_username:
        # character not initialized yet
        return

    username = world_data.char_id_to_username[inflictor]

    if username == "not initialized":
        # self not initialized
        return

    char: Character = world_data.characters[username]

    if nominal < 0:
        if target == inflictor:
            # suicide
            return
        char.update_damage_dealt(abs(nominal))
    else:
        char.update_heal_dealt(nominal)

    ws_update_damage_heal(world_data)


def ws_update_damage_heal(world_data: WorldData):
    event = {
        "type": "update_dps",
        "payload": {"party_members": world_data.serialize_party_members()},
    }
    send_event(event)
