import json
import os

jonPath = os.path.join(
    os.path.dirname(__file__), "../../resources/ao-bin-dumps-json/harvestables.json"
)

with open(jonPath) as json_file:
    harvestables_by_id = json.load(json_file)



class HarvestablesInfo:
    @classmethod
    def get_harvestables_id(cls, code: int):
        try:
            return harvestables_by_id["AO-Harvestables"]["Harvestable"][code]
        except Exception as e:
            print(e)
            return None
        
    def get_harvestables_by_name(cls, name: str):
        try:
            for item in harvestables_by_id["AO-Harvestables"]["Harvestable"]:
                if item.get("@name") == name:
                    return item
            return None
        except Exception as e:
            print(e)
            return None

