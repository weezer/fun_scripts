def end_to_end(m, n):

    """peeling"""

    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]
    #using character for testing. pls do not use more than 93 units.
    cha_lst = [chr(i + 33) for i in range(m * n)]
    two_d = list(chunks(cha_lst, n))
    # two_d = [[1,2,3], [4,5,6], [7,8,9]]
    for i in two_d:
        print i

    x_axis = len(two_d) - 1
    y_axis = 0
    d1 = len(two_d) - 1
    d2 = len(two_d[0]) - 1
    ret = []
    direction = 'u'

    if m < 1 or n < 1:
        return False
    if n == 1:
        for i in range(m-1, -1, -1):
            ret.append(two_d[i][0])
        return ret
    if m == 1:
        return two_d[0]

    while x_axis != 0 or y_axis != d2:
        if x_axis > 0 and direction == 'u':
            ret.append(two_d[x_axis][y_axis])
            x_axis -= 1
            direction = 'r'
        elif y_axis < d2:
            ret.append(two_d[x_axis][y_axis])
            y_axis += 1
            direction = 'r'

        #lower right
        while y_axis < d2 and x_axis < d1:
            ret.append(two_d[x_axis][y_axis])
            x_axis += 1
            y_axis += 1

        if y_axis < d2 and direction == 'r':
            ret.append(two_d[x_axis][y_axis])
            y_axis += 1
            direction = 'u'
        elif x_axis > 0:
            ret.append(two_d[x_axis][y_axis])
            x_axis -= 1
            direction = 'u'
        #upper left
        while y_axis > 0 and x_axis > 0:
            ret.append(two_d[x_axis][y_axis])
            x_axis -= 1
            y_axis -= 1
    ret.append(two_d[0][d2])
    print ret
end_to_end(5, 2)