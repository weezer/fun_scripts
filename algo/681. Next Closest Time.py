def next_closest_time(input_time):
    lst = []
    for i in input_time:
        if i.isdigit():
            lst.append(i)
    first_half = int(input_time[:2])
    second_half = int(input_time[3:])
    #take care digit 4
    for i in lst:
        i_34 = input_time[3]
        if i > input_time[4]:
            i_34 += i
            if int(i_34) < 60:
                return input_time[:4] + i

    #take care digit 3
    for i in lst:
        i_34 = input_time[4]
        if i > input_time[3]:
            i_34 = i + i_34
            if int(i_34) < 60:
                return input_time[:3] + i + input_time[4:]

    #take care digit 2
    for i in lst:
        i_12 = input_time[0]
        if i > input_time[1]:
            i_12 += i
            if int(i_12) < 24:
                return input_time[:1] + i + input_time[2:]

    #take care digit 1
    for i in lst:
        i_12 = input_time[1]
        if i > input_time[0]:
            i_12 = i + i_12
            if int(i_12) < 24:
                return i + input_time[1:]

    min_n = min(lst)
    return min_n + min_n + ":" + min_n + min_n

print next_closest_time("19:34")