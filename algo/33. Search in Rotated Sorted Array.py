class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        lower = 0
        higher = len(nums) - 1
        while lower <= higher:
            mid = (lower + higher) / 2
            print lower, mid, higher
            if nums[lower] == target:
                return lower
            if nums[higher] == target:
                return higher
            if nums[mid] == target:
                return mid
            if mid == higher:
                return -1
            if nums[lower] < nums[mid] < nums[higher]:
                if nums[higher] > target > nums[mid]:
                    lower = mid + 1
                else:
                    higher = mid
            elif nums[lower] > nums[higher] > nums[mid]:

                if nums[higher] > target > nums[mid]:
                    lower = mid + 1
                else:
                    higher = mid
            elif nums[mid] > nums[lower] > nums[higher]:
                if nums[lower] < target < nums[mid]:
                    higher = mid
                else:
                    lower = mid + 1
            else:
                lower += 1

if __name__ == "__main__":
    s = Solution()
    for i in range(10):
        print s.search([9,1,2,3,4,5,6,7,8], i)
