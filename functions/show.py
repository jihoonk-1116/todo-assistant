def parse_check(b):
    return "[ ]" if b else "[v]"

def show(todos):
    for k, v in todos.items():
        print(f"{parse_check(v)} {k[0]}. {k[1]}".replace("\n", ""))
    return