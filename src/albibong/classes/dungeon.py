from datetime import datetime
import uuid

DIVISOR = 10000


class Dungeon:

    def __init__(self, type, name) -> None:
        self.id = uuid.uuid4()
        self.type = type
        self.name = name
        self.tier = 0
        self.fame_gained = 0
        self.silver_gained = 0
        self.re_spec_gained = 0
        self.loot = []
        self.start_time = datetime.now()
        self.time_elapsed = 0

    @staticmethod
    def serialize(dungeon):
        return {
            "id": str(dungeon.id),
            "type": dungeon.type,
            "name": dungeon.name,
            "tier": dungeon.tier,
            "fame": dungeon.fame_gained,
            "silver": dungeon.silver_gained,
            "re_spec": dungeon.re_spec_gained,
            "date_time": dungeon.start_time.strftime("%a %d %b %Y, %I:%M%p"),
            "time_elapsed": str(dungeon.time_elapsed).split(".")[0],
        }

    @staticmethod
    def serialize_many(dungeons):
        serialized = []
        for key, value in dungeons.items():
            serialized.append(Dungeon.serialize(value))
        return serialized

    def get_elapsed_time(self):
        end_time = datetime.now()
        self.time_elapsed = end_time - self.start_time

    def update_fame(self, parameters):
        fame = parameters[2] / DIVISOR
        self.fame_gained += fame

    def update_re_spec(self, parameters):
        re_spec = parameters[2] / DIVISOR
        self.re_spec_gained += re_spec

    def update_loot(self, parameters):
        if 3 in parameters and parameters[3] == True:
            silver = parameters[5] / DIVISOR
            self.silver_gained += silver
        else:
            self.loot.append(parameters[4])
