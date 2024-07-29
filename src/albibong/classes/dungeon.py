from datetime import datetime
import uuid
from peewee import *

from albibong.models.models import BaseModel

DIVISOR = 10000


class Dungeon(BaseModel):

    # def __init__(self, type, name) -> None:
    #     self.id = uuid.uuid4()
    #     self.type = type
    #     self.name = name
    #     self.tier = 0
    #     self.fame_gained = 0
    #     self.silver_gained = 0
    #     self.re_spec_gained = 0
    #     self.loot = []
    #     self.start_time = datetime.now()
    #     self.time_elapsed = 0

    id = UUIDField(unique=True, default=uuid.uuid4())
    type = CharField()
    name = CharField()
    tier = IntegerField(default=0)
    fame = FloatField(default=0)
    silver = FloatField(default=0)
    re_spec = FloatField(default=0)
    start_time = DateTimeField(default=datetime.now)
    end_time = DateTimeField(null=True, default=None)

    @staticmethod
    def serialize(dungeon):
        return {
            "id": str(dungeon.id),
            "type": dungeon.type,
            "name": dungeon.name,
            "tier": dungeon.tier,
            "fame": dungeon.fame,
            "silver": dungeon.silver,
            "re_spec": dungeon.re_spec,
            "date_time": dungeon.date_time.strftime("%a %d %b %Y, %I:%M%p"),
            "time_elapsed": str(dungeon.end_time - dungeon.start_time).split(".")[0],
        }

    @staticmethod
    def serialize_many(dungeons):
        serialized = []
        for key, value in dungeons.items():
            serialized.append(Dungeon.serialize(value))
        return serialized

    def set_end_time(self):
        self.end_time = datetime.now()

    def update_fame(self, parameters):
        fame = parameters[2] / DIVISOR
        self.fame += fame
        # me: Dungeon = Dungeon.get(Dungeon.id == self.id)
        # me.fame = self.fame
        # me.save()

    def update_re_spec(self, parameters):
        re_spec = parameters[2] / DIVISOR
        self.re_spec += re_spec

    def update_loot(self, parameters):
        if 3 in parameters and parameters[3] == True:
            silver = parameters[5] / DIVISOR
            self.silver += silver
        # else:
        #     self.loot.append(parameters[4])
