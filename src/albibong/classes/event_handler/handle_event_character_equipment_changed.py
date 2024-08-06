from albibong.classes.event_handler.world_data_utils import WorldDataUtils
from albibong.classes.world_data import WorldData


def handle_event_character_equipment_changed(world_data: WorldData, parameters):
    if 2 in parameters:
        if parameters[0] in world_data.char_id_to_username:
            if world_data.char_id_to_username[parameters[0]] != "not initialized":
                char = world_data.characters[
                    world_data.char_id_to_username[parameters[0]]
                ]
                if char.username in world_data.party_members:
                    char.update_equipment(parameters[2])
                    WorldDataUtils.ws_update_damage_meter(world_data)
        else:
            world_data.change_equipment_log[parameters[0]] = parameters[2]
