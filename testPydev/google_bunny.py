def power_supply(nums):
    result = 0
    negative_num = 0
    max_negative_num = None
    for i in nums:
        if i != 0:
            if result == 0:
                result = i
            else:
                result *= i
        if i < 0:
            negative_num += 1
            max_negative_num = max(i, max_negative_num)
    if negative_num % 2 != 0:
        result = result / max_negative_num
    return result

print power_supply([-2])