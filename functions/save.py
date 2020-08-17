import json

def unparse(todos):
    ret = []
    for _, l in todos.items():
        for item in l:
            ret.append({"context": item.context, "priority": item.priority, "checked_off": item.checked_off})
    
    return {"todos": ret}
    

def save(filename, todos):
    unparsed_todos = unparse(todos)
    with open(filename, "w") as output:
        output.write(json.dumps(unparsed_todos))
        