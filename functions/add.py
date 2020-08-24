from model.todo import Todo

def add(todos, context, priority):
    priority_map = {'h':'high', 'm':'medium', 'l':'medium'}
    priority = priority_map.get(priority)
    todo = Todo(context, False, priority)
    todos[priority].append(todo)
    
    print("{} has been added.".format(context))

    return
