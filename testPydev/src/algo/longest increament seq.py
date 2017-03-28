def LIS(nums):
    nums_len = len(nums)
    result = [1] * nums_len
    for i in range(1, nums_len):
        for j in range(i):
            if nums[i] > nums[j] and result[i] <= result[j]:
                result[i] = result[j] + 1
    return result


print LIS([2,  5,  6,  2,  3,  4,  7,  4])
