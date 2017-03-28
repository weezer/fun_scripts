def geometric_seq(h, q):
    geometric_list = [2**i - 1 for i in range(1, h+1)] + [-1]
    return_lst = []
    print geometric_list

    def find_the_parent(num):
        len_gl = len(geometric_list)-2
        result = []
        while num != 0:
            while geometric_list[len_gl] <= num:
                result.append(geometric_list[len_gl])
                num -= geometric_list[len_gl]
            len_gl -= 1
        if result[-1] == result[-2]:
            return sum(result) + 1
        else:
            return sum(result) + result[-1] + 1

    for i in q:
        if i in geometric_list:
            return_lst.append(geometric_list[geometric_list.index(i) + 1])
        else:
            return_lst.append(find_the_parent(i))
    print return_lst

geometric_seq(5, [21, 4, 30, 26])






