from functions.uncheck import uncheck
from functions.show import show
from utils import general_utils

def uncheck_mode(todos):
    entered = ""
    while len(todos["checked_off"]) > 0:
        general_utils.print_prompt()
        show(todos)
        print("Which todo you would like to uncheck? (ex: c1)\nWhen you are done, enter 'x'.")
        entered = input()
        if entered == "x":
            return

        uncheck(todos, entered)

    print("Everything is unchecked, returning back to main menu")