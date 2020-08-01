from functions.show import show
from functions.add import add
from functions.check_off import check_off
from functions.delete import delete
from functions.parse_todos import parse

todos = parse("todo_list.json")

show(todos)

# while True:
#     print("Do you want me to check off any from the list? Enter the corresponding number to check off.")
#     print("If you want to exit this program, enter x")
#     show(todos)
#     entered = str(input())
#     if entered == '0':
#         todos = add(todos)
#     if entered == 'x':
#         break
#     if entered == 'd':
#         todos = delete(todos)

# print("Bye")

# show(todos)

