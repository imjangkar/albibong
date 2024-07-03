import json
import os

itemsJsonPath = os.path.join(os.path.dirname(__file__), "../resources/items.json")
with open(itemsJsonPath) as json_file:
    item_data = json.load(json_file)


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

    @staticmethod
    def serialize(item):
        return {
            "id": item.id,
            "name": item.name,
            "unique_name": item.unique_name,
            "image": item.image,
        }

    @staticmethod
    def serialize_many(items):
        serialized = []
        for item in items:
            serialized.append(Item.serialize(item))
        return serialized

    @classmethod
    def get_item_from_code(cls, code: str):
        item = item_data[code]

        return cls(id=item["id"], name=item["name"], unique_name=item["unique_name"])
