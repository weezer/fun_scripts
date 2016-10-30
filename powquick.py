def quickpow(a, n):
    ret = 1
    while n > 0:
        if n % 2 == 1:
            ret = ret * a
        a = a * a
        n = n / 2
    return ret


print quickpow(2, 7)