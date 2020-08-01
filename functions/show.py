def parse_check(b):
    return "[v]" if b else "[ ]"

def show(todos):
    counter = 1

    for todo in todos:
        todo["number"] = counter
        counter += 1

    for todo in todos:
        print(f'{parse_check(todo["checked_off"])} {todo["number"]}. {todo["todo"]}')
