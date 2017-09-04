def quicksort(nums, start, end):
    if end - start < 1:
        return
    pivot = nums[start]
    left = start + 1
    right = end
    while left < right:
        if nums[left] <= pivot and nums[right] > pivot:
            left += 1
            right -= 1
        elif nums[left] <= pivot and nums[right] <= pivot:
            left += 1
        elif nums[left] > pivot and nums[right] <= pivot:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1
        else:
            right -= 1
    if left == right and nums[left] > pivot:
        left = left - 1
        temp = nums[start]
        nums[start] = nums[left]
        nums[left] = temp
    elif left == right and nums[left] <= pivot:
        temp = nums[start]
        nums[start] = nums[left]
        nums[left] = temp
    else:
        left = left - 1
        temp = nums[start]
        nums[start] = nums[left]
        nums[left] = temp
    quicksort(nums, start, left-1)
    quicksort(nums, right, end)
    print nums

quicksort([4,3], 0, len([4,3]) - 1)