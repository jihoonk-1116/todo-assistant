import json

from functions.show import show
from functions.add import add
from functions.check_off import check_off
from functions.deletion import deletion

def get_item(todos, n):
    for k, v in todos.items():
        if k[0] == n:
            return k

    return None

todos = {}
with open("todo_list.json", "r") as todo_input:
    todos = json.load(todo_input)["todos"]


while True:
    print("Do you want me to check off any from the list? Enter the corresponding number to check off.")
    print("If you want to exit this program, enter x")
    show(todos)
    entered = str(input())
    if entered == '0':
        todos = add(todos)
    if entered == 'x':
        break
    if entered == 'd':
        todos = deletion(todos)

print("Bye")

show(todos)

