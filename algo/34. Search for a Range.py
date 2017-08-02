class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_nums = len(nums)
        left = 0
        right = len_nums - 1
        start = 0
        end = len_nums - 1
        if len_nums == 0 or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] < target < nums[mid + 1]:
                return [-1, -1]
            if nums[mid] > target:
                right = mid
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    start = mid
                    break
                right = mid
            if nums[mid] < target:
                left = mid + 1
        if start + 1 == len_nums or nums[start + 1] != target:
            return [start, start]
        left = start
        right = end
        while left <= right:
            mid = (left + right) / 2 + 1
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] == target:
                if mid == len_nums-1 or nums[mid + 1] != target:
                    end = mid
                    break
                left = mid
            if nums[mid] < target:
                left = mid
        return [start, end]

if __name__ == "__main__":
    s = Solution()
    print s.searchRange([5,5 ,7,7,7,7,8,8,10, 10], 8)
    print s.searchRange([1,5], 4)
    print s.searchRange([2,2], 2)
    print s.searchRange([1,3], 1)
    print s.searchRange([0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10], 4)
    print s.searchRange([3,3,3], 3)