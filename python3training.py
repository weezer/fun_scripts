def list():
    global stack1
    stack1 = [555]
    bbb = [5,6,7]
    def inner_func():
        global stack1
        print stack1
        stack1 = [1,2,3,4]
        bbb = [9,9,9]
        print stack1
        print "inner finished"
    inner_func()
    print stack1
    print bbb

list()