import os

def print_prompt():
    os.system('cls||clear')
    print("---------------------------------------------------------")
    print("Select an option (When you are done, enter 'x'):\n1. Check off\n2. Uncheck\n3. Add\n4. Delete\n5. Change priority")
    print("---------------------------------------------------------")

def parse_and_validate_user_input(todos, user_input):
    priority_map = {"h": "high", "m": "medium", "l": "low"}
    priority, index = user_input[0], int(user_input[1:])
    if priority == 'c':
        return (None, index - 1)
    elif validate_user_input(todos, priority_map.get(priority), index):
        return (priority_map.get(priority), index - 1)

    return (None, -1)

def validate_user_input(todos, todo_type, index):
    target_type = todos[todo_type]
    if len(target_type) < index:
        return False
    
    return True

def getch():
    import termios
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    return _getch()