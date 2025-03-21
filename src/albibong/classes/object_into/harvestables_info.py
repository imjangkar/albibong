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

