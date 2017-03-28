def answer(num):
    def split_number(large, small):
        number_list = []
        while small < large:
            number_list.append([small, large])
            small += 1
            large -= 1
        return number_list
    return_answer = []
    import Queue
    q = Queue.deque()
    for i in range(1, (num+1)/2):
        q.append([i, num-i])
    return_answer.extend(q)
    while q:
        small, large = q.pop()
        num_list = split_number(small+1, large-2)
        small = [small]
        for i in num_list:
            if not small[:].extend(i) in return_answer:
                return_answer.append(small[:].extend(i))
            q.append(i)



    print return_answer

answer(10)
