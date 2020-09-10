import actions
import os
import json
import time

todo_file = "todo_list.json"

with open(todo_file, "r") as f:
    todos = json.load(f)

while True:
    os.system('clear')
    actions.show(todos)
    print(f"{'Select an option (Press x to save and exit)':<59}")
    print("1:Check\n2:Uncheck\n3.Add\n4:Delete")

    entered = input("❯ ")

    if entered == '1':
        actions.check(todos)
    elif entered == '2':
        actions.uncheck(todos)
    elif entered == '3':
        actions.add(todos)
    elif entered == '4':
        actions.remove(todos)
    elif entered == 'x':
        with open(todo_file, "w") as output:
            output.write(json.dumps(todos, indent=4))
        break
    else:
        print("ERROR: Invalid input. Please select a valid option")
        time.sleep(1)
        continue
    