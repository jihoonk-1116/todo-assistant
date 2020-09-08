
def remove(todos, priority, index):

   target_todo = todos.get(priority)[index]
   del todos.get(priority)[index]

   return target_todo.context