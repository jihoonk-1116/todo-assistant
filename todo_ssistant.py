import json

from functions.show import show
from functions.add import add
from functions.check_off import check_off

def get_item(todos, n):
    for k, v in todos.items():
        if k[0] == n:
            return k

    return None

todos = {}
with open("todo_list.json", "r") as todo_input:
    todos = json.load(todo_input)["todos"]

counter = 1

for todo in todos:
    todo["number"] = counter
    counter += 1

show(todos)
print("Do you want me to check off any from the list? Enter the corresponding number to check off.")
entered = input()

item = get_item(todos, entered)

check_off(todos, item)
show(todos)
