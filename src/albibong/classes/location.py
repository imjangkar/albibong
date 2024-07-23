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

    @classmethod
    def get_location_from_code(cls, code: str):
        location = map_data[code]

        return cls(id=location["id"], name=location["name"], type=location["type"])
