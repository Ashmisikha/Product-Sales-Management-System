import json

DB_FILE = "database.json"

def load_data():
    try:
        with open(DB_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"products": [], "sales": []}

def save_data(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)
