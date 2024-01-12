import json


def to_json(items):
    if not isinstance(items, list):
        items = [items]  # Convert single object to a list
    return json.dumps([item.to_dict() for item in items])
