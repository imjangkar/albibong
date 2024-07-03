from datetime import timedelta
import json
import os
from collections import deque
import threading
from uuid import UUID
from playsound import playsound

from albibong.classes.character import Character
from albibong.classes.coords import Coords
from albibong.classes.dungeon import Dungeon
from albibong.classes.item import Item
from albibong.classes.location import Location
from albibong.classes.utils import Utils
from albibong.resources.EventCode import EventCode
from albibong.resources.OperationCode import OperationCode
from albibong.threads.websocket_server import send_event

FILENAME = os.path.join(os.path.expanduser("~"), "Albibong/list_dungeon.json")
os.makedirs(os.path.dirname(FILENAME), exist_ok=True)


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

    def end_current_dungeon(self):
        if self.current_dungeon:
            list_dungeon = deque()

            try:
                with open(FILENAME) as json_file:
                    list_dungeon = deque(json.load(json_file))
            except:
                pass

            self.current_dungeon.get_elapsed_time()
            list_dungeon.appendleft(Dungeon.serialize(self.current_dungeon))

            with open(FILENAME, "w") as json_file:
                json.dump(list(list_dungeon), json_file)

            event = {
                "type": "update_dungeon",
                "payload": {"list_dungeon": list(list_dungeon)},
            }
            send_event(event)
            self.current_dungeon = None

    def start_current_dungeon(self, type, name):
        if self.current_dungeon == None:
            new_dungeon = Dungeon(type, name)
            self.current_dungeon = new_dungeon

    def set_dungeon_status(self, check_map, map_type_splitted):
        if "EXPEDITION" in map_type_splitted or "DUNGEON" in map_type_splitted:
            self.start_current_dungeon(type=check_map.type, name=check_map.name)
        elif (
            "EXPEDITION" not in map_type_splitted or "DUNGEON" not in map_type_splitted
        ):
            self.end_current_dungeon()
            return False

    def convert_id_to_name(self, old_id, new_id, char: Character):
        if old_id in self.char_id_to_username:
            self.char_id_to_username.pop(old_id)  # delete old relative id
        char.id = new_id
        self.char_id_to_username[char.id] = char.username  # add new relative id

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
