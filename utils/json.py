import json


def to_json(items):
    return json.dumps([item.to_dict() for item in items])
