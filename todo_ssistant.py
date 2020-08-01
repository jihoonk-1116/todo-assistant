from functions.show import show
from functions.add import add
from functions.check_off import check_off
from functions.deletion import deletion

todos = {}
with open("todo_list.txt", "r") as todo_input:
    lines = todo_input.readlines()
    for line in lines:
        todos[tuple(line.split(". "))] = True

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

print("Have a nice day!")