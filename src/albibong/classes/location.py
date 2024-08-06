import json
import os
import stat
import uuid
from datetime import date, datetime, timedelta

from peewee import CharField, DateTimeField, UUIDField, fn
from playhouse.sqlite_ext import JSONField

from albibong.classes.dungeon import Dungeon
from albibong.classes.item import Item
from albibong.models.models import BaseModel

mapsJsonPath = os.path.join(os.path.dirname(__file__), "../resources/maps.json")
with open(mapsJsonPath) as json_file:
    map_data = json.load(json_file)


class Location(BaseModel):

    uuid = UUIDField(unique=True, default=uuid.uuid4)
    id = CharField()
    name = CharField()
    type = CharField()

    @classmethod
    def get_location_from_code(cls, code: str):
        location = map_data[code]

        return cls(id=location["id"], name=location["name"], type=location["type"])


class Island(Location, BaseModel):

    uuid = UUIDField(unique=True, default=uuid.uuid4)
    id = CharField()
    name = CharField()
    type = CharField()
    start_time = DateTimeField(default=datetime.now)
    crops = JSONField(default=dict)
    animals = JSONField(default=dict)

    def add_crop(self, unique_name, quantity):
        crop = Item.get_item_from_unique_name(unique_name)

        if crop.name not in self.crops:
            self.crops[crop.name] = Item.serialize(crop)

        self.crops[crop.name]["quantity"] += quantity

    def add_animal(self, unique_name, quantity):
        animal = Item.get_item_from_unique_name(unique_name)

        if animal.name not in self.animals:
            self.animals[animal.name] = Item.serialize(animal)

        self.animals[animal.name]["quantity"] += quantity

    @staticmethod
    def serialize(island):
        data = {
            "id": str(island.uuid),
            "name": island.name,
            "type": island.type,
            "date_time": island.start_time.strftime("%a %d %b %Y, %I:%M%p"),
            "crops": island.serialize_crops(),
            "animals": island.serialize_animals(),
        }
        return data

    def serialize_animals(self):
        serialized = []

        for key, value in self.animals.items():
            serialized.append(value)

        return serialized

    def serialize_crops(self):
        serialized = []

        for key, value in self.crops.items():
            serialized.append(value)

        return serialized

    @staticmethod
    def get_all_island():
        query = Island.select().order_by(Island.start_time.desc())
        a = [Island.serialize(island) for island in query]
        return a

    @staticmethod
    def get_total_harvest_by_date(date=datetime.today()):

        date = date
        tomorrow = date + timedelta(days=1)

        query = Island.select().where(
            Island.start_time >= date.date(),
            Island.start_time < tomorrow.date(),
        )

        total_crops = {}
        total_animals = {}

        for island in query:

            crops = island.crops
            for key, value in crops.items():
                if key not in total_crops:
                    total_crops[key] = {
                        "name": key,
                        "quantity": value["quantity"],
                        "image": value["image"],
                    }
                else:
                    total_crops[key]["quantity"] += value["quantity"]

            animals = island.animals
            for key, value in animals.items():
                if key not in total_animals:
                    total_animals[key] = {
                        "name": key,
                        "quantity": value["quantity"],
                        "image": value["image"],
                    }
                else:
                    total_animals[key]["quantity"] += value["quantity"]

        crops_result = []
        for key, value in total_crops.items():
            crops_result.append(value)

        animals_result = []
        for key, value in total_animals.items():
            animals_result.append(value)

        return {
            "crops": crops_result,
            "animals": animals_result,
            "date": str(date.date()),
        }

    @staticmethod
    def get_island_from_code(code: str):
        island = map_data[code]

        obj = Island(id=island["id"], name=island["name"], type=island["type"])

        return obj
