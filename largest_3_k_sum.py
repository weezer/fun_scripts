import random

def largest_3_k_sum(nums, k):
    stack = [0] * (len(nums) - k + 1)
    len_stack = len(stack)
    for i in range(len_stack):
        stack[i] = nums[i:i+k]
    print stack
    global max_result
    max_result = []

    def dfs(num_stack, result_stack):
        global max_result
        if len(result_stack) > 3:
            return
        # print result_stack
        max_result = (max_result, result_stack[:])[sum(map(sum, result_stack)) > sum(map(sum, max_result))]
        for i in range(len(num_stack)):
            copy_result_stack = result_stack[:]
            copy_result_stack.append(num_stack[i])
            start_point = (0, i-k)[i-k > 0]
            copy_num_stack = num_stack[:start_point] + num_stack[i+k:]
            dfs(copy_num_stack, copy_result_stack)
    dfs(stack, [])
    print max_result

def pair_sum_maximum_for_3(arr):
    size = len(arr)
    if size == 0 : return 0
    a = [0] * (size-1)
    for i in range(1, size):
        a[i-1] = arr[i-1] + arr[i]

    dp = [a]
    dp.append([0] * len(a))
    dp.append([0] * len(a))

    ma = max(a[:2])

    for i in range(2, len(a)):
        if i == 2:
            dp[1][i] = a[0] + a[i]
        else:
            dp[1][i] = ma + a[i]
            
    ma = dp[1][2]
    for i in range(4, len(a)):
        ma = max(ma, dp[1][i-2])
        dp[2][i] = ma + a[i]

    print dp
    print max(dp[2])

arr = [1, 2, 4, 2, 1, 5, 8, 4, 2, 8, 9, 9]
arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 9, 8, 8]
arr=arr[::-1]
pair_sum_maximum_for_3(arr)


if __name__ == "__main__":
    test_stack = []
    for i in range(40):
        test_stack.append(random.randint(1, 9))
    pair_sum_maximum_for_3([1,2,3,4,8,9,5,2,7])



