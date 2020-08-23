import time

from functions.uncheck import uncheck
from functions.show import show
from utils import general_utils

def uncheck_mode(todos):
    entered = ""
    while len(todos["checked_off"]) > 0:
        general_utils.print_prompt()
        show(todos)
        entered = input("Which todo you would like to uncheck? (ex: c1)\nWhen you are done, enter 'x': ")
        if entered == "x":
            return

        index = general_utils.parse_and_validate_user_input(todos, entered)[1]
        if index < 0:
            print("ERROR: Please enter a valid input.")
            time.sleep(1)
            continue
        uncheck(todos, index)

    print("Everything is unchecked, returning back to main menu")
    time.sleep(1)