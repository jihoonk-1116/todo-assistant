import time

from functions.check_off import check_off
from functions.show import show
from utils import general_utils

def check_off_mode(todos):
    entered = ""
    while True:
        general_utils.print_prompt()
        show(todos)
        entered = input("Which todo you would like to check off? (ex: h1)\nWhen you are done, enter 'x': ")
        if entered == "x":
            return
        else:
            try:
                priority, index = general_utils.parse_and_validate_user_input(todos, entered)
            except:
                print("ERROR: Please enter a valid input.")
                time.sleep(1)
                continue
            if priority:
                check_off(todos, priority, index)
            else:
                print("ERROR: Please enter a valid input.")
                time.sleep(1)