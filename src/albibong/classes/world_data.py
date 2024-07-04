from uuid import UUID

from albibong.classes.character import Character
from albibong.classes.coords import Coords
from albibong.classes.dungeon import Dungeon
from albibong.classes.item import Item
from albibong.classes.location import Location


class WorldData:

    def __init__(self) -> None:
        self.me: Character = Character(
            id=None,
            uuid=None,
            username="not initialized",
            guild="not initialized",
            alliance="not initialized",
            coords=Coords(0, 0),
        )
        self.current_map: Location = None
        self.current_dungeon: Dungeon = None
        self.characters: dict[str, Character] = {}
        self.char_id_to_username: dict[int, str] = {self.me.id: self.me.username}
        self.char_uuid_to_username: dict[UUID, str] = {self.me.uuid: self.me.username}
        self.change_equipment_log: dict[int, list] = {}
        self.party_members: set[str] = set()
        self.is_dps_meter_running: bool = True

    def serialize_party_members(self):
        serialized = []

        total_damage = 0
        total_heal = 0

        # get total damage and heal for percentage
        for key, value in self.characters.items():
            if key in self.party_members:
                total_damage += value.damage_dealt
                total_heal += value.healing_dealt

        for member in self.party_members:
            # member character initialized
            if member in self.characters:
                char = self.characters[member]
                username = char.username
                damage_dealt = char.damage_dealt
                damage_percent = (
                    round(char.damage_dealt / total_damage * 100, 2)
                    if total_damage > 0
                    else 0
                )
                healing_dealt = char.healing_dealt
                heal_percent = (
                    round(char.healing_dealt / total_heal * 100, 2)
                    if total_heal > 0
                    else 0
                )
                duration = char.total_combat_duration

                combat_duration = str(duration).split(".")[0]
                dps = (
                    damage_dealt // duration.total_seconds()
                    if duration.total_seconds() != 0
                    else 0
                )
                weapon = (
                    Item.serialize(char.equipment[0])["image"]
                    if char.equipment != []
                    else "/No Equipment.png"
                )

            # member character not initialized
            else:
                username = member
                damage_dealt = 0
                damage_percent = 0
                healing_dealt = 0
                heal_percent = 0
                combat_duration = 0
                dps = 0
                weapon = "/No Equipment.png"

            data = {
                "username": username,
                "damage_dealt": damage_dealt,
                "damage_percent": damage_percent,
                "healing_dealt": healing_dealt,
                "heal_percent": heal_percent,
                "combat_duration": combat_duration,
                "dps": dps,
                "weapon": weapon,
            }
            serialized.append(data)
        serialized.sort(key=lambda x: x["damage_dealt"], reverse=True)
        return serialized


world_data = WorldData()


def get_world_data():
    return world_data
