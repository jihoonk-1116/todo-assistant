from functions.add import add
from utils import general_utils
from functions.show import show
import time


def validate(input):
    return input == 'h' or input == 'm' or input == 'l'

def add_mode(todos):
    entered = ""
    while True:
        show(todos)
        context = input("Please enter a new todo (ex:meeting at 3PM) : ")
        priority = input("Please enter its priority.(ex: h, m, l) : ") 
        
        while not validate(priority): #Check validation
            priority = input("ERROR: Please enter a valid priority(h,m,l) : ")

        print(f"Check your new todo: '{context}', Priority: '{priority}' \nIs is correct? (y/n) (If you like to stop adding, enter 'x')")
        ans = general_utils.getch()

        if ans == 'x':
            break
        if ans == 'n':
            continue
        
        add(todos, context, priority)

        print("Would you like to add more todo? (y/n)")
        ans = general_utils.getch()
        if ans == 'y':
            general_utils.print_prompt()
            continue
        if ans == 'n':
            break