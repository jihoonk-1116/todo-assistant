def delete(todos):
    print("Enter the priority number what you want to remove")
    enter = str(input())
    print(todos)
    index = int(enter[1])-1
    if enter[0] == 'h':
        for i,v in enumerate(todos['high']):
            if index == i:
                del todos['high'][i]
    if enter[0] == 'm':
        for i,v in enumerate(todos['medium']):
            if index == i:
                del todos['medium'][i]
    if enter[0] == 'l':
        for i,v in enumerate(todos['low']):
            if index == i:
                del todos['low'][i]
    return todos