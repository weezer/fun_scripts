def simplify(lst):
    bracket = 0
    saved_position = []
    for i in range(1, len(lst)):
        if lst[i] is not '(' and lst[i-1] is '(':
            bracket += 1
            saved_position.append(i-1)
        if bracket != 0 and lst[i] is ')':
            saved_position.append(i)
            bracket -= 1
        


