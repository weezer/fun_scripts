def binarysearch(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right) / 2
        if right == mid and nums[mid] != target:
            break
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid
        if nums[mid] < target:
            left = mid + 1
    return -1

a = [1,2,3,4,6]
b = 5
print binarysearch(a, b)
