from utils import general_utils

def check_off(todos, user_input):
    priority_map = {"h": "high", "m": "medium", "l": "low"}
    
    priority, index = general_utils.parse_user_input(user_input)

    todo_to_move = todos.get(priority_map.get(priority))[index]
    todo_to_move.checked_off = True
    todos.get("checked_off").append(todo_to_move)
    
    del todos.get(priority_map.get(priority))[index]

    return