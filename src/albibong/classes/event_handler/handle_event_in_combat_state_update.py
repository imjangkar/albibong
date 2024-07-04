from albibong.classes.character import Character
from albibong.classes.world_data import WorldData


def handle_event_in_combat_state_update(world_data: WorldData, parameters):

    if parameters[0] not in world_data.char_id_to_username:
        # character not initialized
        return

    name = world_data.char_id_to_username[parameters[0]]
    char: Character = world_data.characters[name]

    if 1 in parameters:
        char.update_combat_duration(True)
    else:
        char.update_combat_duration(False)
