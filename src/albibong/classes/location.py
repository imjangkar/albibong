import json
import os

mapsJsonPath = os.path.join(os.path.dirname(__file__), "../resources/maps.json")
with open(mapsJsonPath) as json_file:
    map_data = json.load(json_file)


class Location:

    def __init__(self, id: str, name: str, type: str):
        self.id = id
        self.name = name
        self.type = type

    def is_black_zone(self):
        if self.type == "OPENPVP_BLACK":
            return True
        elif self.type == "DUNGEON_BLACK":
            return True
        elif self.type == "PASSAGE_BLACK":
            return True
        elif self.type == "TUNNEL":
            return True
        else:
            return False

    def is_red_zone(self):
        if self.type == "OPENPVP_RED":
            return True
        elif self.type == "DUNGEON_RED":
            return True
        elif self.type == "PASSAGE_RED":
            return True
        else:
            return False

    def is_safe_zone(self):
        if self.is_black_zone() == False and self.is_red_zone() == False:
            return True
        else:
            return False

    @classmethod
    def get_location_from_code(cls, code: str):
        location = map_data[code]

        return cls(id=location["id"], name=location["name"], type=location["type"])
