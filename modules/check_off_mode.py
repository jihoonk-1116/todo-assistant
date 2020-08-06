from functions.check_off import check_off
def check_off_mode(todos):
    entered = ""
    while entered != "x":
        print("Please tell me which todo you would like to check off (ex: h1)")
        entered = input()
        check_off(todos, entered)