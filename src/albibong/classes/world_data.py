import json
import os
from collections import deque
from uuid import UUID

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

    def handle_response(self, parameters):
        if 253 in parameters:
            if parameters[253] == OperationCode.JOIN.value:
                self.handle_join_response(parameters)
            elif parameters[253] == OperationCode.CHANGE_CLUSTER.value:
                self.set_location(parameters)
            # elif parameters[253] == OperationCode.PARTY_LEAVE.value:
            #     self.party_members = set(self.me.username)

    def handle_event(self, parameters):
        if 252 in parameters:
            if parameters[252] == EventCode.OTHER_GRABBED_LOOT.value:
                if 2 in parameters and parameters[2] in self.characters:
                    char: Character = self.characters[parameters[2]]
                    char.update_loot(parameters)
                if self.current_dungeon and parameters[2] == self.me.username:
                    self.current_dungeon.update_loot(parameters)
            elif parameters[252] == EventCode.UPDATE_FAME.value:
                self.me.update_fame(parameters)
                if self.current_dungeon:
                    self.current_dungeon.update_fame(parameters)
            elif parameters[252] == EventCode.UPDATE_RE_SPEC_POINTS.value:
                self.me.update_re_spec(parameters)
                if self.current_dungeon:
                    self.current_dungeon.update_re_spec(parameters)
            elif parameters[252] == EventCode.CHARACTER_EQUIPMENT_CHANGED.value:
                self.change_character_equipment(parameters)
            elif (
                parameters[252] == EventCode.HEALTH_UPDATE.value
                and self.is_dps_meter_running
            ):
                self.update_dps_meter(parameters)
            elif (
                parameters[252] == EventCode.PARTY_JOINED.value
                or parameters[252] == EventCode.PARTY_PLAYER_JOINED.value
                or parameters[252] == EventCode.PARTY_PLAYER_LEFT.value
                or parameters[252] == EventCode.PARTY_DISBANDED.value
            ):
                self.update_party_member(parameters)
            elif parameters[252] == EventCode.NEW_CHARACTER.value:
                self.create_character(
                    id=parameters[0],
                    uuid=parameters[7],
                    username=parameters[1],
                    guild=parameters[8] if 8 in parameters else "",
                    alliance=parameters[49] if 49 in parameters else "",
                    coords=(
                        Coords(parameters[15][0], parameters[15][1])
                        if 15 in parameters
                        else Coords(0, 0)
                    ),
                    equipments=parameters[38] if 38 in parameters else [],
                )
        ...

    def handle_request(self, parameters):
        if 253 in parameters:
            if parameters[253] == OperationCode.MOVE.value and self.me:
                self.me.update_coords(parameters)
        ...

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

    def set_location(self, parameters):
        self.change_equipment_log = {}

        if 1 in parameters:
            check_map = Location.get_location_from_code(parameters[1])
            map_type_splitted = set(check_map.type.split("_"))
            self.set_dungeon_status(check_map, map_type_splitted)

            if "ISLAND" in map_type_splitted or "HIDEOUT" in map_type_splitted:
                check_map.name = f"{parameters[2]}'s {check_map.name}"
                self.current_map = check_map

        elif 0 in parameters:
            check_map = Location.get_location_from_code(parameters[0])
            map_type_splitted = set(check_map.type.split("_"))
            is_dungeon = self.set_dungeon_status(check_map, map_type_splitted)
            if is_dungeon == False:
                self.current_map = Location.get_location_from_code(parameters[0])

        event = {
            "type": "update_location",
            "payload": {
                "map": self.current_map.name if self.current_map else "None",
                "dungeon": (
                    self.current_dungeon.name if self.current_dungeon else "None"
                ),
            },
        }
        send_event(event)

    def update_party_member(self, parameters):
        if parameters[252] == EventCode.PARTY_JOINED.value:
            self.party_members = set(parameters[5])
        elif parameters[252] == EventCode.PARTY_DISBANDED.value:
            self.party_members = set()
        elif parameters[252] == EventCode.PARTY_PLAYER_JOINED.value:
            self.party_members.add(parameters[2])
        elif parameters[252] == EventCode.PARTY_PLAYER_LEFT.value:
            uuid = UUID(bytes=bytes(parameters[1]))
            if uuid in self.char_uuid_to_username:
                name = self.char_uuid_to_username[uuid]
                if name == self.me.username:
                    self.party_members = set()
        if self.me.id != None:
            self.party_members.add(self.me.username)
        event = {
            "type": "update_dps",
            "payload": {"party_members": self.serialize_party_members()},
        }
        send_event(event)

    def update_dps_meter(self, parameters):
        if 6 in parameters and parameters[6] in self.char_id_to_username:
            username = self.char_id_to_username[parameters[6]]
            if username in self.party_members:
                char: Character = self.characters[username]
                char.handle_health_update(parameters)
                event = {
                    "type": "update_dps",
                    "payload": {"party_members": self.serialize_party_members()},
                }
                send_event(event)

    def change_character_equipment(self, parameters):
        if 2 in parameters:
            if parameters[0] in self.char_id_to_username:
                if self.char_id_to_username[parameters[0]] != "not initialized":
                    char = self.characters[self.char_id_to_username[parameters[0]]]
                    if char.username in self.party_members:
                        char.update_equipment(parameters[2])
                        event = {
                            "type": "update_dps",
                            "payload": {
                                "party_members": self.serialize_party_members()
                            },
                        }
                        send_event(event)
            else:
                self.change_equipment_log[parameters[0]] = parameters[2]

    def handle_join_response(self, parameters):
        # set my character

        self.convert_id_to_name(old_id=self.me.id, new_id=parameters[0], char=self.me)

        self.me.uuid = Utils.convert_int_arr_to_uuid(parameters[1])
        self.me.username = parameters[2]
        self.me.guild = parameters[57] if 57 in parameters else ""
        self.me.alliance = parameters[77] if 77 in parameters else ""
        self.characters[self.me.username] = self.me
        self.char_uuid_to_username[self.me.uuid] = self.me.username
        if self.me.id in self.change_equipment_log:
            self.me.update_equipment(self.change_equipment_log[self.me.id])

        # set map my character is currently in
        if parameters[8][0] == "@":
            area = parameters[8].split("@")
            if area[1] == "RANDOMDUNGEON":
                check_map = Location.get_location_from_code(area[1])
                self.start_current_dungeon(type=check_map.type, name=check_map.name)

        event_char = {
            "type": "init_character",
            "payload": {
                "username": self.me.username,
                "fame": self.me.fame_gained,
                "re_spec": self.me.re_spec_gained,
                "silver": self.me.silver_gained,
                "weapon": self.me.equipment[0].image,
            },
        }
        event_map = {
            "type": "update_location",
            "payload": {
                "map": self.current_map.name if self.current_map else "None",
                "dungeon": (
                    Dungeon.serialize(self.current_dungeon)
                    if self.current_dungeon
                    else None
                ),
            },
        }
        send_event(event_map)
        send_event(event_char)

    def convert_id_to_name(self, old_id, new_id, char: Character):
        if old_id in self.char_id_to_username:
            self.char_id_to_username.pop(old_id)  # delete old relative id
        char.id = new_id
        self.char_id_to_username[char.id] = char.username  # add new relative id

    def create_character(
        self,
        id: int,
        uuid: list[int],
        username: str,
        guild: str,
        alliance: str,
        equipments: list[str] = [],
        coords: Coords = Coords(0, 0),
    ):

        # initiate character
        if username not in self.characters:
            char: Character = Character(
                id=id,
                uuid=Utils.convert_int_arr_to_uuid(uuid),
                username=username,
                guild=guild,
                alliance=alliance,
                coords=coords,
            )
            char.update_equipment(equipments)
            self.characters[char.username] = char
            self.char_id_to_username[char.id] = char.username
            self.char_uuid_to_username[char.uuid] = char.username

        # change map
        else:
            char: Character = self.characters[username]
            char.update_equipment(equipments)
            char.coords = coords
            self.convert_id_to_name(old_id=char.id, new_id=id, char=char)

    def serialize_party_members(self):
        serialized = []

        total_damage = 0
        total_heal = 0
        for key, value in self.characters.items():
            if key in self.party_members:
                total_damage += value.damage_dealt
                total_heal += value.healing_dealt

        for key, value in self.characters.items():
            if key in self.party_members:
                if value.equipment != []:
                    weapon = Item.serialize(value.equipment[0])["image"]
                    data = {
                        "username": value.username,
                        "damage_dealt": value.damage_dealt,
                        "damage_percent": (
                            round(value.damage_dealt / total_damage * 100, 2)
                            if total_damage > 0
                            else 0
                        ),
                        "healing_dealt": value.healing_dealt,
                        "heal_percent": (
                            round(value.healing_dealt / total_heal * 100, 2)
                            if total_heal > 0
                            else 0
                        ),
                        "weapon": weapon,
                    }
                    serialized.append(data)
        serialized.sort(key=lambda x: x["damage_dealt"], reverse=True)
        return serialized


world_data = WorldData()


def get_world_data():
    return world_data
