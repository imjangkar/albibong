import uuid
from datetime import datetime

from peewee import *

from albibong.models.models import BaseModel

DIVISOR = 10000


class Dungeon(BaseModel):

    id = UUIDField(unique=True, default=uuid.uuid4)
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
            "date_time": dungeon.start_time.strftime("%a %d %b %Y, %I:%M%p"),
            "time_elapsed": (
                str(dungeon.end_time - dungeon.start_time).split(".")[0]
                if dungeon.end_time
                else ""
            ),
        }

    def set_end_time(self):
        self.end_time = datetime.now()

    def update_fame(self, parameters):
        fame = parameters[2] / DIVISOR
        self.fame += fame

    def update_re_spec(self, parameters):
        re_spec = parameters[2] / DIVISOR
        self.re_spec += re_spec

    def update_loot(self, parameters):
        if 3 in parameters and parameters[3] == True:
            silver = parameters[5] / DIVISOR
            self.silver += silver

    @staticmethod
    def get_all_dungeon():
        query = Dungeon.select().order_by(Dungeon.start_time.desc())
        return [Dungeon.serialize(dungeon) for dungeon in query]
