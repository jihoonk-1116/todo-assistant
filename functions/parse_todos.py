import json

def parse(filename):
    high = []
    medium = []
    low = []
    checked_off = []
    
    with open(filename, "r") as f:
        input_todos = json.load(f)["todos"]
        for todo in input_todos:
            if todo["checked_off"]:
                checked_off.append((todo["todo"], todo["checked_off"]))
            elif todo["priority"] == "high":
                high.append((todo["todo"], todo["checked_off"]))
            elif todo["priority"] == "medium":
                medium.append((todo["todo"], todo["checked_off"]))
            elif todo["priority"] == "low":
                low.append((todo["todo"], todo["checked_off"]))
            else:
                print(f"Invalid priority for {todo}")

    todos = {"high": high, "medium": medium, "low": low, "checked_off": checked_off}

    return todos