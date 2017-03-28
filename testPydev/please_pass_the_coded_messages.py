def answer(nums):
    result_list = []
    mod_one_and_two = []
    for i in nums:
        if i % 3 == 0:
            result_list.append(i)
        else:
            mod_one_and_two.append(i)

    combination_result = combination(mod_one_and_two)
    max_list = []
    max_num = 0
    sum_num = 0
    for i in combination_result:
        if len(i) >= max_num and sum(i) % 3 == 0 and sum(i) > sum_num:
            max_list = i
            max_num = len(i)
            sum_num = sum(i)

    result_list.extend(max_list)
    result_list.sort()
    multiplier = 1
    result = 0
    for i in result_list:
        result += multiplier*i
        multiplier *= 10
    return result


def combination(nums):
    answer = [[]]
    for i in nums:
        for j in range(len(answer)):
            copy_answer = answer[j][:]
            copy_answer.append(i)
            answer.append(copy_answer)
    return answer


def permutation(nums):
    answer = [[]]
    for i in nums:
        for j in range(len(answer)):
            copy_answer = answer[j][:]
            for z in range(len(copy_answer) + 1):
                p_answer = copy_answer[:z] + [i] + copy_answer[z:]
                answer.append(p_answer)
    return answer

print answer([2,2,4,4,4])
