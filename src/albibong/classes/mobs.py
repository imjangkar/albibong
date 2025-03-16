import json
import os

mobsByIdJsonPath = os.path.join(
    os.path.dirname(__file__), "../resources/mobs_by_id.json"
)

with open(mobsByIdJsonPath) as json_file:
    mobs_by_id = json.load(json_file)



class MobInfo:
    @classmethod
    def get_mob_from_code(cls, code: str):
        return mobs_by_id.get(code, None)
