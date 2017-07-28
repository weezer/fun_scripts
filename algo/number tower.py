def tower(input_lst):
    result = input_lst[len(input_lst) - 1][:]
    for i in range(len(input_lst)-2, -1, -1):
        for j in range(i+1):
            result[j] = max(result[j], result[j+1]) + input_lst[i][j]

    print result[0]


tower([[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]])