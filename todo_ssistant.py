from functions.show import show
from functions.add import add
from functions.check_off import check_off
from functions.delete import delete
from functions.parse_todos import parse
from modules.check_off_mode import check_off_mode
from modules.uncheck_mode import uncheck_mode
from utils import general_utils
import os

todos = parse("todo_list.json")
os.system('cls||clear')
general_utils.print_prompt()

while True:
    show(todos)
# Do input validation here, priority letter & index
    entered = general_utils.getch()

    if entered == '1':
        general_utils.print_prompt()
        check_off_mode(todos)
        general_utils.print_prompt()
    elif entered == '2':
        general_utils.print_prompt()
        uncheck_mode(todos)
        general_utils.print_prompt()
    elif entered == '3':
        break
    elif entered == '4':
        break
    elif entered == 'x':
        #save here
        break
    else:
        general_utils.print_prompt()
        print("Invalid input. Please select a valid option\n")


