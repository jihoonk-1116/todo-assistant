import json
from model.todo import Todo

def parse(filename):
    high = []
    medium = []
    low = []
    checked_off = []
    
    with open(filename, "r") as f:
        input_todos = json.load(f)["todos"]
        for input_todo in input_todos:
            todo = Todo(input_todo["context"], input_todo["checked_off"], input_todo["priority"])
            if todo.checked_off:
                checked_off.append(todo)
            elif todo.priority == "high":
                high.append(todo)
            elif todo.priority == "medium":
                medium.append(todo)
            elif todo.priority == "low":
                low.append(todo)
            else:
                print(f"Invalid priority for \"{todo.context}\"")

    todos = {"high": high, "medium": medium, "low": low, "checked_off": checked_off}

    return todos