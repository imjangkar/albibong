from albibong.models.models import BaseModel
from albibong.threads.websocket_server import send_event

class Radar(BaseModel):
    def __init__(self) -> None:
        self.position = {"x": 0, "y": 0}
        self.harvestable_list = []
    
    def update_position(self, x, y):
        self.position = {"x": x, "y": y}

        event = {
            "type": "radar_position_update",
            "payload": {
                "position": self.position
            }
        }

        send_event(event)
    
    def add_harvestable(self, id, type, tier, posX, posY, enchant, size):
        # ID 1: Standard enchanted resource
        # ID 2: From Dead Mob resource
        FIBER_IDS = [14,15,16] # Standard, From Spotk lokation, dead mob
        WOOD_IDS = [0]
        ROCK_IDS = [7]
        HIDE_IDS = [20]
        ORE_IDS = [27, 29]
        
        unique_name = ""
        item_type = "unknown"

        
        if(type in FIBER_IDS):
            item_type = "FIBER"
            unique_name = f"T{tier}_{item_type}" if enchant == 0 else f"T{tier}_{item_type}_LEVEL{enchant}@{enchant}"
        elif(type in WOOD_IDS):
            item_type = "WOOD"
            unique_name = f"T{tier}_{item_type}" if enchant == 0 else f"T{tier}_{item_type}_LEVEL{enchant}@{enchant}"
        elif(type in ROCK_IDS):
            item_type = "ROCK"
            unique_name = f"T{tier}_{item_type}" if enchant == 0 else f"T{tier}_{item_type}_LEVEL{enchant}@{enchant}"
        elif(type in HIDE_IDS):
            item_type = "HIDE"
            unique_name = f"T{tier}_{item_type}" if enchant == 0 else f"T{tier}_{item_type}_LEVEL{enchant}@{enchant}"
        elif(type in ORE_IDS):
            item_type = "ORE"
            unique_name = f"T{tier}_{item_type}" if enchant == 0 else f"T{tier}_{item_type}_LEVEL{enchant}@{enchant}"

        
        # if (type >= 11 and type <= 14):
        #     item_type = "FIBER"
        #     unique_name = f"T{tier}_{item_type}" if enchant == 0 else f"T{tier}_{item_type}_LEVEL{enchant}@{enchant}"
        # elif (type >= 0 and type <= 5):
        #     item_type = "WOOD"
        #     unique_name = f"T{tier}_{item_type}" if enchant == 0 else f"T{tier}_{item_type}_LEVEL{enchant}@{enchant}"
        # elif (type >= 6 and type <= 10):
        #     item_type = "ROCK"
        #     unique_name = f"T{tier}_{item_type}" if enchant == 0 else f"T{tier}_{item_type}_LEVEL{enchant}@{enchant}"
        # elif (type >= 15 and type <= 22):
        #     item_type = "HIDE"
        #     unique_name = f"T{tier}_{item_type}" if enchant == 0 else f"T{tier}_{item_type}_LEVEL{enchant}@{enchant}"
        # elif (type >= 23 and type <= 27):
        #     item_type = "ORE"
        #     unique_name = f"T{tier}_{item_type}" if enchant == 0 else f"T{tier}_{item_type}_LEVEL{enchant}@{enchant}"

        self.harvestable_list.append({
            "id": id,
            "type": type,
            "tier": tier,
            "location": {
                "x": posX,
                "y": posY
            },
            "enchant": enchant,
            "size": size,
            "item_type": item_type,
            "unique_name": unique_name
        })

        self.__handle_update()

    
    def update_harvestable(self, id, count):
        for harvestable in self.harvestable_list:
            if harvestable["id"] == id:
                harvestable["size"] = count
        
        self.__handle_update()

    def serialize(self):
        return {
            "harvestable_list": self.harvestable_list
        }

    def change_location(self):
        self.harvestable_list = []
        self.update_position(0, 0)
        self.__handle_update()

    def __handle_update(self):
        payload = self.serialize()
        event = {
            "type": "radar_update",
            "payload": payload
        }

        send_event(event)