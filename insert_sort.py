def insert_sort(nums):
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    print nums

insert_sort([5,4,1,2,3])
