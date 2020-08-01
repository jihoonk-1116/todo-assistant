def add(todos):
    print("Enter To do list")
    enter = str(input())
    index = str(len(todos) +1)
    todos[(index,enter)] = True
    return todos
