class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target or nums[left] == target or nums[right] == target:
                return True
            if nums[mid] < nums[right]:
                if nums[right] > target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > nums[right] :
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right -= 1
        return False