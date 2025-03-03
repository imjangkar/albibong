import os
import json

# Use items https://github.com/ao-data/ao-bin-dumps/blob/master/formatted/items.txt
# save it as items.txt
# Run this script to generate items_by_id.json and items_by_unique_name.json

def item_by_id(item):
    return {
        item[0]: {
            "id": item[0],
            "unique_name": item[1],
            "name": item[2],
        },
    }

def item_by_unique_name(item):
    return {
        item[1]: {
            "id": item[0],
            "unique_name": item[1],
            "name": item[2],
        },
    }

def load_items(file_path):
    items = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split(':')
            if len(parts) == 3:
                item_id = parts[0].strip()
                item_code = parts[1].strip()
                item_name = parts[2].strip()
                items.append((item_id, item_code, item_name))
    return items

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), 'items.txt')
    items = load_items(file_path)
    
    items_by_id = {}
    items_by_unique_name = {}
    
    for item in items:
        items_by_id.update(item_by_id(item))
        items_by_unique_name.update(item_by_unique_name(item))

    with open('items_by_id.json', 'w') as json_file:
        json.dump(items_by_id, json_file, indent=4)

    with open('items_by_unique_name.json', 'w') as json_file:
        json.dump(items_by_unique_name, json_file, indent=4)