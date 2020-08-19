from utils import general_utils

def check_off(todos, priority, index):

    todo_to_move = todos.get(priority)[index]
    todo_to_move.checked_off = True
    todos.get("checked_off").append(todo_to_move)
    
    del todos.get(priority)[index]

    return