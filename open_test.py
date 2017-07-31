def outside():
    a = 123
    def inside():
        print a
    inside()
    print "out" + str(a)

outside()