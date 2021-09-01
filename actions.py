from datetime import datetime, timedelta
import os
import time

def print_and_wait(s):
    print(s)
    time.sleep(1)

def print_error():
    print_and_wait("ERROR: Invalid response. Please enter a valid input")

def show(todos):
    os.system('clear')

    start_range = datetime.now() - timedelta(days=5)
    
    print("──────────────────────────────── 🔻 ───────────────────────────────────")

    for i, todo in enumerate(todos.get("unchecked")):
        print(f"[{i+1:>2}] {todo.get('context'):56}{todo.get('timestamp')}")

    print("──────────────────────────────── ✅ ───────────────────────────────────")

    for i, todo in enumerate(todos.get("checked")):
        if datetime.strptime(todo.get("timestamp"), "%m/%d/%Y") > start_range:
            print(f"[{i+1:>2}] {todo.get('context'):56}{todo.get('timestamp')}")

    print("───────────────────────────────────────────────────────────────────────\n")


def remove(todos):
    show(todos)
    while True:
        entered = input("Which list? (1: Todo 2: Finished, entere 'x' to exit): ")
        if entered == '1':
            category = "unchecked"
        elif entered == '2':
            category = "checked"
        elif entered == 'x':
            return
        else:
            print_error()
            continue

        if len(todos.get(category)) == 0:
            print_and_wait(f"'{category}' is empty")
            continue
        
        entered = input("Which one do you want to remove? (Enter 'x' to cancel): ")
        if entered == 'x':
            return

        index = int(entered)
        if index > len(todos.get(category)):
            print_error()
            continue

        context = todos.get(category)[index - 1].get("context")

        while True:
            entered = input(f"Removing '{context}'. Proceed? (y/n): ")
            if entered == 'n':
                break
            elif entered == 'y':
                del todos.get(category)[index - 1]
                print_and_wait(f"'{context}' has been removed.")
                show(todos)
                break
            else:
                print_error()
    
def uncheck(todos):
    while len(todos.get("checked")) > 0:
        show(todos)
        entered = input("Which one to uncheck? (Enter 'x' to exit): ")

        if entered == "x":
            return
        try:
            index = int(entered)
        except:
            print_error()
            continue

        if index > len(todos.get("checked")):
            print_error()
            continue

        todos.get("unchecked").append(todos.get("checked")[index - 1])
        del todos.get("checked")[index - 1]

    print_and_wait("Everything is checked, returning back to the main menu")

def check(todos):
    while len(todos.get("unchecked")) > 0:
        show(todos)
        entered = input("Which one to uncheck? (Enter 'x' to exit): ")

        if entered == "x":
            return
        try:
            index = int(entered)
        except:
            print_error()
            continue

        if index > len(todos.get("unchecked")):
            print_error()
            continue

        todos.get("checked").append(todos.get("unchecked")[index - 1])
        del todos.get("unchecked")[index - 1]

    print_and_wait("Everything is checked, returning back to the main menu")

def add(todos):
    while True:
        show(todos)
        context = input("What do you need to do? (Enter 'x' to exit): ")

        if context == 'x':
            return
        elif not context:
            print_error()
            continue

        while True:
            entered = input(f"'{context}'. Proceed? (y/n): ")
            if entered == 'n':
                break
            elif entered == 'y':
                todos.get("unchecked").append({"context": context, "timestamp": datetime.today().strftime("%m/%d/%Y")})
                print_and_wait(f"'{context}' has been added")
                break
            else:
                print_error()