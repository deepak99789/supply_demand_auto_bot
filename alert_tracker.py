import json, os

FILE = "alerts.json"

def is_duplicate(key):
    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            json.dump([], f)

    with open(FILE, "r") as f:
        data = json.load(f)

    if key in data:
        return True

    data.append(key)
    with open(FILE, "w") as f:
        json.dump(data, f)

    return False
