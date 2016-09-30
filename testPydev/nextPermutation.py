class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        left = len(nums) - 1
        change = False
        while left > 0:
            left -= 1
            comp_pos = left
            for i in range(left + 1, len(nums)):
                if nums[i] > nums[left]:
                    if comp_pos is left:
                        comp_pos = i
                    if nums[i] < nums[comp_pos]:
                        comp_pos = i
            if nums[left] < nums[comp_pos]:
                temp = nums[left]
                nums[left] = nums[comp_pos]
                nums[comp_pos] = temp
                change =True
                break
        print nums
        start = len(nums) - 1
        if change:
            end = left
        else:
            end = -1
        for i in range(start, end, -1):
            for j in range(end + 1, i):
                # print nums[i], nums[j], j
                # print nums
                if nums[j] > nums[i]:
                    nums[j] += nums[i]
                    nums[i] = nums[j] - nums[i]
                    nums[j] -= nums[i]

        print nums

if __name__ == "__main__":
    s = Solution()
    # s.nextPermutation([1,2,3])
    # s.nextPermutation([1, 3, 2])
    # s.nextPermutation([2, 1, 3])
    # s.nextPermutation([2, 3, 1])
    # s.nextPermutation([3, 1, 2])
    # s.nextPermutation([3, 2, 1])
    s.nextPermutation([5,4,7,5,3,2])
