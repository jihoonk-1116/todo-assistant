def parse_check(b):
    return "[v]" if b else "[ ]"

def show(todos):
    for i, todo in enumerate(todos["high"]):
        print(f'{parse_check(todo[1])} h{i}. {todo[0]}')
    for i, todo in enumerate(todos["medium"]):
        print(f'{parse_check(todo[1])} m{i}. {todo[0]}')
    for i, todo in enumerate(todos["low"]):
        print(f'{parse_check(todo[1])} l{i}. {todo[0]}')
    for i, todo in enumerate(todos["checked_off"]):
        print(f'{parse_check(todo[1])} c{i}. {todo[0]}')