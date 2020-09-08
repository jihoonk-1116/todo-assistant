from functions.show import show
from functions.parse_todos import parse
from functions.save import save
from modules.check_off_mode import check_off_mode
from modules.uncheck_mode import uncheck_mode
from modules.change_priority_mode import change_priority_mode
from modules.remove_mode import remove_mode
from modules.add_mode import add_mode
from utils import general_utils
import os

todo_file_name = "todo_list.json"

todos = parse(todo_file_name)
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
        general_utils.print_prompt()
        add_mode(todos)
        general_utils.print_prompt()
    elif entered == '4':
        general_utils.print_prompt()
        remove_mode(todos)
        general_utils.print_prompt()
    elif entered == '5':
        general_utils.print_prompt()
        change_priority_mode(todos)
        general_utils.print_prompt()
    elif entered == 'x':
        #save(todo_file_name, todos)
        break
    else:
        general_utils.print_prompt()
        print("Invalid input. Please select a valid option\n")


