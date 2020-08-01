def parse_check(b):
    return "[v]" if b else "[ ]"

def show(todos):
    for i, todo in enumerate(todos["high"]):
        print(f'{parse_check(todo["checked_off"])} h{i}. {todo["todo"]}')
