class Solution(object):
    def insert_position(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if target <= nums[left]:
                return left
            if target >= nums[right]:
                return right
            if target >= nums[mid]:

