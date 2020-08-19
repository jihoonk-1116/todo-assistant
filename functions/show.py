def parse_check(b):
    return "[v]" if b else "[ ]"

def show(todos):
    for i, todo in enumerate(todos["high"]):
        print(f'{parse_check(todo.checked_off)} h{i+1}. {todo.context}')
    for i, todo in enumerate(todos["medium"]):
        print(f'{parse_check(todo.checked_off)} m{i+1}. {todo.context}')
    for i, todo in enumerate(todos["low"]):
        print(f'{parse_check(todo.checked_off)} l{i+1}. {todo.context}')
    for i, todo in enumerate(todos["checked_off"]):
        print(f'{parse_check(todo.checked_off)} c{i+1}. {todo.context}')