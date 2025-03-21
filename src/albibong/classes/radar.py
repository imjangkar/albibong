from albibong.models.models import BaseModel
import struct
import time
import threading
from albibong.threads.websocket_server import send_event
from albibong.classes.object_into.harvestables_info import HarvestablesInfo


class Radar(BaseModel):
    def __init__(self) -> None:
        self.settings = {
            "expiration_time": 180, # 3 minutes
            "sync_time": 0.25, # 250 ms
            "clenaing_time": 60 # 1 minute
        }
        self.position = {"x": 0, "y": 0}
        self.harvestable_list = {}
        self.dungeon_list = {}
        self.chest_list = {}
        self.mist_list = {}
        self.mob_list = {}
        self.update_triggered = False
        
        # Call the clening job
        self.start_cleaning_job()
    
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
        time_stamp = time.time() + self.settings["expiration_time"]

        # Remove old list of ids if this will work fine
        # FIBER_IDS = [14,15,16]
        # WOOD_IDS = [0,3]
        # ROCK_IDS = [7,9]
        # HIDE_IDS = [20,23, 48]
        # ORE_IDS = [27, 29]
        
        unique_name = ""
        item_type = "unknown"

        resource_type = HarvestablesInfo.get_harvestables_id(type)
        if resource_type:
            item_type = resource_type["@resource"]
            unique_name = f"{item_type.toLowerCase()}_{tier}_{enchant}"

        self.harvestable_list[id] = {
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
            "unique_name": unique_name,
            "expiration_time": time_stamp,
            "debug": {}
        }

        self.debounce_handle_update()
    
    def update_harvestable(self, id, count):
        time_stamp = time.time() + self.settings["expiration_time"]
        if id in self.harvestable_list:
            self.harvestable_list[id]["size"] = count
            self.harvestable_list[id]["expiration_time"] = time_stamp
            self.debounce_handle_update()

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
            
            self.dungeon_list[id] = {
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
            }

            self.debounce_handle_update()
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

        self.chest_list[id] = {
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
        }

        self.debounce_handle_update()

    def add_mist(self, id, location, name, enchant, parameters):
        self.mist_list[id] = {
            "id": id,
            "location": {
                "x": location[0],
                "y": location[1]
            },
            "name": name,
            "enchant": enchant,
            "debug": parameters,
        }

    def add_mob(self, id, type_id, location, enchant, rarity, parameters):
        # mobInfo = MobInfo.get_mob_from_code(str(type_id))
        mobInfo = None
        # 13 heath 14 healt
        # 21 tier
        self.mob_list[id] = {
            "id": id,
            "type_id": type_id,
            "location": {
                "x": location[0],
                "y": location[1]
            },
            "mob_name": mobInfo["unicname"] if mobInfo else "unknown",
            "mob_type": mobInfo["type"] if mobInfo else 0,
            "mob_tier": mobInfo["tier"] if mobInfo else 0,
            "debug": parameters
        }

        self.debounce_handle_update()

    def handle_event_leave(self, id):
        founded = False

        if id in self.harvestable_list:
            del self.harvestable_list[id]
            founded = True
        if id in self.dungeon_list:
            del self.dungeon_list[id]
            founded = True
        if id in self.chest_list:
            del self.chest_list[id]
            founded = True
        if id in self.mist_list:
            del self.mist_list[id]
            founded = True
        if id in self.mob_list:
            del self.mob_list[id]
            founded = True

        if founded:
            self.debounce_handle_update()

    def handle_event_move(self, id, parameters):
        founded = False

        # Extract position bytes from parameters
        position_bytes = parameters[1][9:17]
        posX, posY = struct.unpack('ff', bytes(position_bytes))

        if id in self.mist_list:
            self.mist_list[id]["location"] = {"x": posX, "y": posY}
            founded = True

        if id in self.mob_list:
            self.mob_list[id]["location"] = {"x": posX, "y": posY}
            founded = True

        if founded:
            self.debounce_handle_update()

    def serialize(self):
        return {
            "harvestable_list": list(self.harvestable_list.values()),
            "dungeon_list": list(self.dungeon_list.values()),
            "chest_list": list(self.chest_list.values()),
            "mist_list": list(self.mist_list.values()),
            "mob_list": list(self.mob_list.values()),
        }

    def change_location(self):
        self.harvestable_list = {}
        self.dungeon_list = {}
        self.chest_list = {}
        self.mist_list = {}
        self.mob_list = {}
        self.update_position(0, 0)
        self.debounce_handle_update()

    def __handle_update(self):
        payload = self.serialize()
        event = {
            "type": "radar_update",
            "payload": payload
        }

        send_event(event)

    def debounce_handle_update(self):
        if not self.update_triggered:
            self.update_triggered = True
            threading.Timer(self.settings["sync_time"], self.__debounced_update).start()

    def __debounced_update(self):
        self.update_triggered = False
        self.__handle_update()

    def clean_expired_harvestables(self):
        current_time = time.time()
        self.harvestable_list = {id: harvestable for id, harvestable in self.harvestable_list.items() if harvestable["expiration_time"] > current_time}
        self.debounce_handle_update()

    def start_cleaning_job(self):
        def job():
            while True:
                self.clean_expired_harvestables()
                time.sleep(self.settings["clenaing_time"])

        thread = threading.Thread(target=job, daemon=True)
        thread.start()