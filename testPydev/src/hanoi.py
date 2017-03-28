def hanoi(start, pivot, end, n):
    if n == 1:
        print "From " + start + " to " + end + " size " + str(n)
        return
    hanoi(start, end, pivot, n-1)
    print "from " + start + " to " + end + " size " + str(n)
    hanoi(pivot, start, end, n-1)


def hanoi2(n, sou, bri, des):
    stack = []
    result = []
    stack.append([n, sou, bri, des])
    while stack:
        item = stack.pop()
        n = item[0]
        sou = item[1]
        bri = item[2]
        des = item[3]
        if item[0] == 1:
            print "move " + sou + " to " + des
        else:  # add to stack in reverse order
            stack.append([n-1, bri, sou, des])
            stack.append([1, sou, bri, des])
            stack.append([n-1, sou, des, bri])

hanoi2(3,'a','b','c')
