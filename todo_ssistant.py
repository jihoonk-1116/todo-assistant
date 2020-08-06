from functions.show import show
from functions.add import add
from functions.check_off import check_off
from functions.delete import delete
from functions.parse_todos import parse
from modules.check_off_mode import check_off_mode

todos = parse("todo_list.json")

while True:
# Do input validation here, priority letter & index
    print("\nSelect an option:\n1. Show todos\n2. Check off\n3. Uncheck\n4. Add\n5. Delete\n6. Change priority")
    entered = input()

    # check_off(todos, entered)
    if entered == '1':
        show(todos)
    elif entered == '2':
        check_off_mode(todos)
    elif entered == '3':
        break
    elif entered == '4':
        break
    elif entered == '5':
        break
    elif entered == '6':
        break
    else:
        print("Invalid input. Please select a valid option")

print("Bye")


