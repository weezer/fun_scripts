import random

def maxSum(matrix):

    n = len(matrix[0])
    if n == 0:
        return 0
    matrix[:] = map(list, zip(*matrix[::-1]))
    n = len(matrix[0])
    if n == 1:
        return sum(matrix)
    if n == 2:
        return abs(matrix[0]) + abs(matrix[1])

    if sum(matrix[0]) > sum(matrix[1]):
        s_1 = 1
        s_2 = 0
    else:
        s_1 = 0
        s_2 = 1

    for i in range(n-2):
        if matrix[s_1] == matrix[s_2]:
            if sum(matrix[s_1]) > sum(matrix[i+2]) and matrix[i+2] != matrix[s_1]:
                s_1 = i+2
            elif sum(matrix[s_1]) < sum(matrix[i+2]) and matrix[i+2] != matrix[s_1]:
                s_2 = i+2
        elif sum(matrix[s_1]) > sum(matrix[i+2]) and matrix[i+2] != matrix[s_1] and matrix[i+2] != matrix[s_2]:
            s_1 = i+2
            s_2 = s_1

    if matrix[s_1] == matrix[s_2]:
        return sum(map(sum(a) for a in matrix))
    sum_nums = sum(map(sum, matrix))
    print s_1, s_2
    if sum(matrix[s_1]) >= 0:
        return sum(sum_nums)
    elif sum(matrix[s_1]) < 0 and sum(matrix[s_2]) > 0:
        sum_nums -= (sum(matrix[s_1]))
    else:
        print sum_nums
        abs_1 = abs(sum(matrix[s_1]))
        abs_2 = abs(sum(matrix[s_2]))
        print abs_1, abs_2
        sum_nums += 2 * (abs_1 + abs_2)
    return sum_nums


if __name__ == "__main__":
    print maxSum([[-1, 1, -1], [-1,1, 1], [1,1,-1]])



