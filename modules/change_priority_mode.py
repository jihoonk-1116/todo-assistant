from functions.change_priority import change_priority
from functions.show import show
from utils import general_utils
import time

def __map_priority(p):
    priority_map = {"h": "high", "m": "medium", "l": "low"}
    if p in priority_map.keys():
        return priority_map.get(p)
    else:
        return None

def change_priority_mode(todos):
    entered = ""
    while True:
        general_utils.print_prompt()
        show(todos)
        entered = input("Which todo you would like to change priority? (ex: h1)\nWhen you are done, enter 'x': ")
        if entered == "x":
            return
        else:
            try:
                priority, index = general_utils.parse_and_validate_user_input(todos, entered)
            except:
                print("ERROR: Please enter a valid input.")
                time.sleep(1)
                continue
            target_priority = input("To what priority would you like to change? ('h': High, 'm': Medium, 'l': Low): ")
            mapped_priority = __map_priority(target_priority)
            if priority and mapped_priority:
                change_priority(todos, priority, index, mapped_priority)
            else:
                print("ERROR: Please enter a valid input.")
                time.sleep(1)