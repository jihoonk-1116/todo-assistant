def deletion(todos):
    print("Enter number what you want to remove")
    enter = int(input()) - 1
    for i, k in enumerate(todos):
        if i == enter:
            del todos[k]
            break
    return todos