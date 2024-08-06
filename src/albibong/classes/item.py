import json
import os

itemsByIdJsonPath = os.path.join(
    os.path.dirname(__file__), "../resources/items_by_id.json"
)
itemsByUniqueNameJsonPath = os.path.join(
    os.path.dirname(__file__), "../resources/items_by_unique_name.json"
)
with open(itemsByIdJsonPath) as json_file:
    items_by_id = json.load(json_file)
with open(itemsByUniqueNameJsonPath) as json_file:
    items_by_unique_name = json.load(json_file)


class Item:

    def __init__(self, id: str, name: str, unique_name: str):
        self.id = id
        self.name = name
        self.unique_name = unique_name
        self.image = (
            "https://render.albiononline.com/v1/item/" + self.unique_name
            if self.unique_name != "None"
            else "/No Equipment.png"
        )
        self.quantity = 0

    @staticmethod
    def serialize(item):
        return {
            "id": item.id,
            "name": item.name,
            "unique_name": item.unique_name,
            "image": item.image,
            "quantity": item.quantity,
        }

    @staticmethod
    def serialize_many(items):
        serialized = []
        for item in items:
            serialized.append(Item.serialize(item))
        return serialized

    @classmethod
    def get_item_from_code(cls, code: str):
        item = items_by_id[code]

        return cls(id=item["id"], name=item["name"], unique_name=item["unique_name"])

    @classmethod
    def get_item_from_unique_name(cls, unique_name: str):
        item = items_by_unique_name[unique_name]

        return cls(id=item["id"], name=item["name"], unique_name=item["unique_name"])
