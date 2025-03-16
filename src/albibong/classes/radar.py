from albibong.models.models import BaseModel
from albibong.threads.websocket_server import send_event

class Radar(BaseModel):
    def __init__(self) -> None:
        self.position = {"x": 0, "y": 0}
        self.harvestable_list = []
        self.dungeon_list = []
        self.chest_list = []
    
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
        FIBER_IDS = [14,15,16] # Standard, From Spotk lokation, dead mob
        WOOD_IDS = [0]
        ROCK_IDS = [7]
        HIDE_IDS = [20]
        ORE_IDS = [27, 29]
        
        unique_name = ""
        item_type = "unknown"
        
        if(type in FIBER_IDS):
            item_type = "FIBER"
            unique_name = f"fiber_{tier}_{enchant}"
        elif(type in WOOD_IDS):
            item_type = "WOOD"
            unique_name = f"Logs_{tier}_{enchant}"
        elif(type in ROCK_IDS):
            item_type = "ROCK"
            unique_name = f"rock_{tier}_{enchant}"
        elif(type in HIDE_IDS):
            item_type = "HIDE"
            unique_name = f"hide_{tier}_{enchant}"
        elif(type in ORE_IDS):
            item_type = "ORE"
            unique_name = f"ore_{tier}_{enchant}"

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

    def test(self):
        return 6

    def add_dungeon(self, id, location, name, enchant, parameters):
        try:
            tier = int(name[1]) if name[0] == "T" else 0
            dungeon_type = "UNKNOW"
            is_consumable = True if "CONSUMABLE" in name else False
            
            # Find the dungeon_type
            if tier != 0:
                if "SOLO" in name:
                    dungeon_type = "SOLO"
                elif "AVALON" in name:
                    dungeon_type = "AVALON"
                else:
                    dungeon_type = "GROUP"
            else:
                if "CORRUPTED" in name:
                    dungeon_type = "CORRUPTED"
                elif "HELLGATE" in name:
                    dungeon_type = "HELLGATE"

            if dungeon_type == "SOLO":
                unique_name = f"solo_dungeon"
            elif dungeon_type == "GROUP":
                unique_name = f"group_dungeon"
            elif dungeon_type == "AVALON":
                unique_name = f"avalon_dungeon"
            elif dungeon_type == "CORRUPTED":
                unique_name = f"corrupted_dungeon"
            elif dungeon_type == "HELLGATE":
                unique_name = f"hellgate_dungeon"
            else:
                unique_name = f"unknown_dungeon"
            
            self.dungeon_list.append({
                "id": id,
                "dungeon_type": dungeon_type,
                "tier": tier,
                "location": {
                "x": location[0],
                "y": location[1]
                },
                "enchant": enchant,
                "name": name,
                "unique_name": unique_name,
                "is_consumable": is_consumable,
                "debug": parameters,
            })

            self.__handle_update()
        except Exception as e:
            print(e)
            print(parameters)

    def add_cheast(self, id, location, name1, name2, parameters):
        chest_name = name2.upper() if "MIST" in name1 else name1.upper()
        enchant = 0

        if "GREEN" in chest_name or "STANDARD" in chest_name:
            enchant = 1
        elif "BLUE" in chest_name or "UNCOMMON" in chest_name:
            enchant = 2
        elif "PURPLE" in chest_name or "RARE" in chest_name:
            enchant = 3
        elif "YELLOW" in chest_name or "LEGENDARY" in chest_name:
            enchant = 4

        self.chest_list.append({
            "id": id,
            "location": {
            "x": location[0],
            "y": location[1]
            },
            "name1": name1,
            "name2": name2,
            "chest_name": chest_name,
            "enchant": enchant,
            "debug": parameters,
        })

        self.__handle_update()

    def serialize(self):
        return {
            "harvestable_list": self.harvestable_list,
            "dungeon_list": self.dungeon_list,
            "chest_list": self.chest_list
        }

    def change_location(self):
        self.harvestable_list = []
        self.dungeon_list = []
        self.chest_list = []
        self.update_position(0, 0)
        self.__handle_update()

    def __handle_update(self):
        payload = self.serialize()
        event = {
            "type": "radar_update",
            "payload": payload
        }

        send_event(event)