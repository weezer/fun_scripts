class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            if nums[left] > target:
                return left
            if mid == right:
                if nums[mid] >= target:
                    return mid
                else:
                    return mid + 1
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1

if __name__ == "__main__":
    s = Solution()
    for i in range(10):
        print s.searchInsert([1,3,5,6], i)