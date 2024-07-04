from datetime import datetime, timedelta
import json
from uuid import UUID

from albibong.classes.coords import Coords
from albibong.classes.item import Item
from albibong.threads.websocket_server import send_event

DIVISOR = 10000


class Character:

    def __init__(
        self,
        id: int,
        uuid: UUID,
        username: str,
        guild: str,
        alliance: str,
        coords: Coords,
        equipment: list[Item] = [Item.get_item_from_code("0")] * 10,
    ):
        # Profile
        self.id = id
        self.uuid = uuid
        self.username = username
        self.guild = guild
        self.alliance = alliance
        self.coords = coords
        self.equipment = equipment

        # Stats
        self.fame_gained: int = 0
        self.re_spec_gained: int = 0
        self.silver_gained: int = 0
        self.loot: list[str] = []

        # Combat
        self.damage_dealt: int = 0
        self.healing_dealt: int = 0
        self.is_already_in_combat: bool = False
        self.start_combat_time: timedelta = timedelta(0, 0)
        self.total_combat_duration: timedelta = timedelta(0, 0)

    def update_combat_duration(self, is_starting_combat):
        if self.is_already_in_combat == False:
            if is_starting_combat == True:
                self.is_already_in_combat = True
                self.start_combat_time = datetime.now()
        else:
            if is_starting_combat == False:
                self.is_already_in_combat = False
                current_combat_duration = datetime.now() - self.start_combat_time
                self.total_combat_duration += current_combat_duration

    def update_damage_dealt(self, nominal):
        if self.is_already_in_combat:
            self.damage_dealt += nominal

    def update_heal_dealt(self, nominal):
        if self.is_already_in_combat:
            self.healing_dealt += nominal

    def update_coords(self, parameters):
        if 3 in parameters:
            self.coords = Coords(parameters[3][0], parameters[3][1])

    def update_fame(self, parameters):
        fame = parameters[2] / DIVISOR
        self.fame_gained += fame
        event = {
            "type": "update_fame",
            "payload": {"username": self.username, "fame_gained": fame},
        }
        send_event(event)

    def update_re_spec(self, parameters):
        re_spec = parameters[2] / DIVISOR
        self.re_spec_gained += re_spec
        event = {
            "type": "update_re_spec",
            "payload": {"username": self.username, "re_spec_gained": re_spec},
        }
        send_event(event)

    def update_loot(self, parameters):
        if 3 in parameters and parameters[3] == True:
            if 5 in parameters:
                silver = parameters[5] / DIVISOR
                self.silver_gained += silver
                event = {
                    "type": "update_silver",
                    "payload": {"username": self.username, "silver_gained": silver},
                }
                send_event(event)
        else:
            self.loot.append(parameters[4])

    def update_equipment(self, equipments):
        new_eq = []
        if equipments != []:
            for eq in equipments:
                obj = Item.get_item_from_code(str(eq))
                new_eq.append(obj)
        self.equipment = new_eq
