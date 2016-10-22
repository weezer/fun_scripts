def binarysearch(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right) / 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid
        if nums[mid] < target:
            left = mid + 1
    return -1

a = [1,2,3,4,5]
b = 4

print binarysearch(a, b)
