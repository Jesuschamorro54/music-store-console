import json
import os
import random

def define_id(path):
    if not os.path.exists(path):
        return random.randint(1000, 9999)

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        used_ids = [item.get("id") for item in data if "id" in item]
        new_id = random.randint(1000, 9999)

        while new_id in used_ids:
            new_id = random.randint(1000, 9999)

        return new_id

    except:
        return random.randint(1000, 9999)


def validate_exist(path, value):
    if not os.path.exists(path):
        return (False, None)

    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except:
            return (False, None)

    for item in data:
        if "id" in item:
            try:
                if int(item["id"]) == int(value):
                    return (True, item["id"])
            except:
                pass

        if isinstance(value, str) and "name" in item:
            if item["name"].strip().lower() == value.strip().lower():
                return (True, item["id"])

    return (False, None)
