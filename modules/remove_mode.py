from utils import general_utils
from functions.show import show
from functions.remove_todo import remove
import time

def __map_priority(p):
    priority_map = {"h": "high", "m": "medium", "l": "low"}
    if p in priority_map.keys():
        return priority_map.get(p)
    else:
        return None

def remove_mode(todos):
    entered = ""
    while True:
        show(todos)
        entered = input("Which todo you would like to remove? (ex:h1)\nWhen you are done, enter 'x' ")
        if entered == 'x':
            return
        elif entered[0] == 'c':
            if len(todos.get("checked_off")) < int(entered[1:]):
                print("ERROR: Please enter a valid input.")
                time.sleep(1)
                continue
            else:
                removed_context = remove(todos, "checked_off", int(entered[1:])-1)
                print('---------------------------------')
                print(f"'{removed_context}' has been removed. ")
                print('---------------------------------')
                time.sleep(1)
                general_utils.print_prompt()
        else:
            try:
                priority, index = general_utils.parse_and_validate_user_input(todos, entered)
            except:
                print("ERROR: Please enter a valid input.")
                time.sleep(1)
                continue
            mapped_priority = __map_priority(entered[0])
            if priority and mapped_priority:
                removed_context = remove(todos, mapped_priority, index)
                print('---------------------------------')
                print(f"'{removed_context}' has been removed. ")
                print('---------------------------------')
                time.sleep(1)
                general_utils.print_prompt()
            else:
                print("ERROR: Please enter a valid input,")
                time.sleep(1)
            