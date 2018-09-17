class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.divide_conquer(0, len(nums)-1, nums)

    def divide_conquer(self, left, right, nums):
        if left == right:
            return nums[left]
        mid = (left + right) / 2
        left_val = self.divide_conquer(left, mid, nums)
        right_val = self.divide_conquer(mid + 1, right, nums)
        crossing = self.find_crossing_sum(left, mid, right+1, nums)

        return max(left_val, right_val, crossing)

    def find_crossing_sum(self, left, mid, right, nums):
        if left == right:
            return nums[left]
        left_val = -float('inf')
        value = 0
        for i in range(mid - 1, left - 1, -1):
            value += nums[i]
            if value > left_val:
                left_val = value
        if left_val < 0:
            left_val = 0
        right_val = -float('inf')
        val = 0
        for i in range(mid, right):
            val += nums[i]
            if val > right_val:
                right_val = val
        return left_val + right_val

if __name__ == "__main__":
    s = Solution()
    print s.maxSubArray([-2,-3])