from utils import general_utils

def change_priority(todos, priority, index, target_priority):

    todo_to_move = todos.get(priority)[index]
    todo_to_move.priority = target_priority
    todos.get(target_priority).append(todo_to_move)
    
    del todos.get(priority)[index]

    return