import uuid
from datetime import datetime

from peewee import *
from playhouse.sqlite_ext import JSONField

from albibong.models.models import BaseModel

DIVISOR = 10000


class Dungeon(BaseModel):

    id = UUIDField(unique=True, default=uuid.uuid4)
    type = CharField()
    name = CharField()
    tier = FloatField(default=0)
    fame = FloatField(default=0)
    silver = FloatField(default=0)
    re_spec = FloatField(default=0)
    might = FloatField(default=0)
    favor = FloatField(default=0)
    start_time = DateTimeField(default=datetime.now)
    end_time = DateTimeField(null=True, default=None)
    meter = JSONField(default=dict)

    @staticmethod
    def serialize(dungeon):
        time_elapsed = dungeon.end_time - dungeon.start_time
        total_hours = time_elapsed.total_seconds() / 3600

        return {
            "id": str(dungeon.id),
            "type": dungeon.type,
            "name": dungeon.name,
            "tier": dungeon.tier,
            "fame": dungeon.fame,
            "fame_per_hour": dungeon.fame / total_hours,
            "silver": dungeon.silver,
            "silver_per_hour": dungeon.silver / total_hours,
            "re_spec": dungeon.re_spec,
            "re_spec_per_hour": dungeon.re_spec / total_hours,
            "might": dungeon.might,
            "might_per_hour": dungeon.might / total_hours,
            "favor": dungeon.favor,
            "favor_per_hour": dungeon.favor / total_hours,
            "date_time": dungeon.start_time.strftime("%a %d %b %Y, %I:%M%p"),
            "time_elapsed": (
                str(time_elapsed).split(".")[0] if dungeon.end_time else ""
            ),
            "meter": dungeon.meter,
        }

    def set_end_time(self):
        self.end_time = datetime.now()

    def update_fame(self, parameters):
        fame = parameters[2] / DIVISOR
        self.fame += fame

    def update_re_spec(self, parameters):
        re_spec = parameters[2] / DIVISOR
        self.re_spec += re_spec

    def update_might_and_favor(self, parameters):
        self.favor += parameters[4] / DIVISOR
        self.might += parameters[1] / DIVISOR

    def update_loot(self, parameters):
        if 3 in parameters and parameters[3] == True:
            silver = parameters[5] / DIVISOR
            self.silver += silver

    def update_meter(self, party):
        self.meter = party

    @staticmethod
    def get_all_dungeon():
        query = Dungeon.select().order_by(Dungeon.start_time.desc())
        return [Dungeon.serialize(dungeon) for dungeon in query]
