def parse_check(b):
    return "[v]" if b else "[ ]"

def show(todos):
    for todo in todos:
        print(f'{parse_check(todo["checked_off"])} {todo["number"]}. {todo["todo"]}')
