def quicksort(nums, start, end):
    if start >= end:
        return
    pivot = nums[start]
    left = start + 1
    right = end
    while left < right:
        if nums[right] < pivot <= nums[left] :
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        elif nums[right] >= pivot > nums[left]:
            left += 1
            right -= 1
        elif nums[left] >= pivot and nums[right] >= pivot:
            right -= 1
        else:
            left += 1
    if left == right and nums[left] < pivot:
        nums[start], nums[left] = nums[left], nums[start]
    if left == right and nums[left] > pivot:
        nums[start], nums[left-1] = nums[left-1], nums[start]
        left -= 1
    if left > right:
        nums[start], nums[left-1] = nums[left-1], nums[start]
        left -= 1
    quicksort(nums, start, left - 1)
    quicksort(nums, left + 1, end)

a = [i for i in range(2,-1,-1)]
a = [1,5,6,3,1,8,6]
print a
quicksort(a, 0, len(a) - 1)
print a

import collections
collections.deque()