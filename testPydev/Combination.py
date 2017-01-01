answer = []

def combination(array, n):
    for i in range(len(array)):
        recursive_comb([array[i]], array[i+1:], n)


def recursive_comb(temp_array, rest_array, n):
    if len(temp_array) == n:
        answer.append(temp_array)
        return
    for i in range(len(rest_array)):
        temp_array2 = temp_array[:]
        temp_array2.append(rest_array[i])
        recursive_comb(temp_array2, rest_array[i+1:], n)


combination([3,4], 2)
print answer
