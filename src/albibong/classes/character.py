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
        self.id = id
        self.uuid = uuid
        self.username = username
        self.guild = guild
        self.alliance = alliance
        self.coords = coords
        self.fame_gained: int = 0
        self.re_spec_gained: int = 0
        self.silver_gained: int = 0
        self.damage_dealt: int = 0
        self.healing_dealt: int = 0
        self.loot: list[str] = []
        self.equipment = equipment

    def handle_health_update(self, parameters):
        if 2 in parameters:
            if parameters[2] < 0:
                if parameters[0] != self.id:
                    self.damage_dealt += abs(parameters[2])
            else:
                self.healing_dealt += abs(parameters[2])

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
