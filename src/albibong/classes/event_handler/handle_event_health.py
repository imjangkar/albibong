from albibong.classes.character import Character
from albibong.classes.event_handler.world_data_utils import WorldDataUtils
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

    WorldDataUtils.update_damage_or_heal(world_data, target, inflictor, nominal)


def handle_event_health_updates(world_data: WorldData, parameters):

    if world_data.is_dps_meter_running == False:
        return

    if 0 not in parameters or 6 not in parameters or 2 not in parameters:
        return

    for i in range(len(parameters[2])):
        nominal = parameters[2][i]
        target = parameters[0]
        inflictor = parameters[6][i]

        WorldDataUtils.update_damage_or_heal(world_data, target, inflictor, nominal)
