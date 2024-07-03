from albibong.classes.character import Character
from albibong.classes.world_data import WorldData


def handle_event_other_grabbed_loot(world_data: WorldData, parameters):

    # update char data
    if 2 in parameters and parameters[2] in world_data.characters:
        char: Character = world_data.characters[parameters[2]]
        char.update_loot(parameters)

    # update dungeon data
    if world_data.current_dungeon and parameters[2] == world_data.me.username:
        world_data.current_dungeon.update_loot(parameters)
