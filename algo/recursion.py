def recursin(num):
    if num < 100:
        num += 1
        recursin(num)
    print num

recursin(1)