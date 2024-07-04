from albibong.classes.character import Character
from albibong.classes.coords import Coords
from albibong.classes.event_handler.world_data_utils import WorldDataUtils
from albibong.classes.utils import Utils
from albibong.classes.world_data import WorldData


def handle_event_new_character(world_data: WorldData, parameters):

    id = parameters[0]
    uuid = parameters[7]
    username = parameters[1]
    guild = parameters[8] if 8 in parameters else ""
    alliance = parameters[49] if 49 in parameters else ""
    coords = (
        Coords(parameters[15][0], parameters[15][1])
        if 15 in parameters
        else Coords(0, 0)
    )
    equipments = parameters[38] if 38 in parameters else []

    # initiate character
    if username not in world_data.characters:
        char: Character = Character(
            id=id,
            uuid=Utils.convert_int_arr_to_uuid(uuid),
            username=username,
            guild=guild,
            alliance=alliance,
            coords=coords,
        )
        char.update_equipment(equipments)
        world_data.characters[char.username] = char
        world_data.char_id_to_username[char.id] = char.username
        world_data.char_uuid_to_username[char.uuid] = char.username

    # change map
    else:
        char: Character = world_data.characters[username]
        char.update_equipment(equipments)
        char.coords = coords
        WorldDataUtils.convert_id_to_name(
            world_data, old_id=char.id, new_id=id, char=char
        )
