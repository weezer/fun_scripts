class Solution(object):
    def insert_position(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if target <= nums[left]:
                return left
            if target >= nums[right]:
                return right + 1
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                left = mid + 1
            if target < nums[mid]:
                right = mid - 1


if __name__ == "__main__":
    s = Solution()
    print s.insert_position([1, 4, 6, 8,9, 11, 13, 16], 14)


