def add(todos):
    print("Enter To do list and priority(h,m,l)")
    enter = str(input())
    prior = str(input())
    #todos[pri][list][key]
    if prior == 'h':
        todos['high'].append((enter,False))
    if prior == 'm':
        todos['medium'].append((enter,False))
    if prior == 'l':
        todos['low'].append((enter,False))

    return todos
