import json

from functions.show import show
from functions.add import add
from functions.check_off import check_off
from functions.deletion import deletion
from functions.parse_todos import parse

high = []
medium = []
low = []
checked_off = []
todos = {"high": high, "medium": medium, "low": low, "checked_off": checked_off}


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

