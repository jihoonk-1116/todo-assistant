from functions.show import show
from functions.add import add
from functions.check_off import check_off

todos = {}
with open("todo_list.txt", "r") as todo_input:
    lines = todo_input.readlines()
    for line in lines:
        todos[tuple(line.split(". "))] = True

show(todos)
print("Do you want me to check off any from the list? Enter the corresponding number to check off.")
entered = input()
show(todos)