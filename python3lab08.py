def return_even_stringodd(start, stop):
    while start <= stop:
        if start % 2 == 0:
            yield "odd"
        else:
            yield start
        start += 1

# for i in return_even_stringodd(4, 10):
#     print i

a = return_even_stringodd(1, 10)
while True:
    try:
        print next(a)
    except StopIteration:
        print 'next finished'
        break
