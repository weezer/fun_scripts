def check_prime(n):
    prime_list = [0 for i in range(n+1)]
    prime_list[1] = True
    for i in range(2, n):
        multiple = 0
        if prime_list[i] is 0:
            prime_list[i] = True
            prime_num = i
            multiple = n / prime_num
        if multiple != 0:
            for j in range(2, multiple):
                prime_list[i * j] = False
    for i in range(1, n):
        if prime_list[i] is True:
            print i


check_prime(30)


