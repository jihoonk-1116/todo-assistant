from utils import general_utils

def uncheck(todos, user_input):    
    todo_to_move = todos.get("checked_off")[index]
    todo_to_move.checked_off = False
    todos.get(todo_to_move.priority).append(todo_to_move)
    
    del todos.get("checked_off")[index]

    return