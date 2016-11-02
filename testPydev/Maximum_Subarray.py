class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = -1 << 31
        tmp_sum = 0
        max_list = [nums[0]]
        for i in nums:
            tmp_sum = max(tmp_sum + i, i)
            max_value = max(max_value, tmp_sum)
        return max_value

if __name__ == "__main__":
    s = Solution()
    print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])