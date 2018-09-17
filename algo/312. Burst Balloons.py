class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for j in xrange(n + 2)] for i in xrange(n + 2)]

        def DP(i, j):
            if i > j:
                return 0
            if dp[i][j] > 0: return dp[i][j]
            for x in xrange(i, j + 1):
                dp[i][j] = max(dp[i][j], DP(i, x - 1) + nums[i - 1] * nums[x] * nums[j + 1] + DP(x + 1, j))
            return dp[i][j]

        a = DP(1, n)
        for i in dp:
            print [str(j).ljust(3) for j in i]

if __name__ == "__main__":
    s = Solution()
    print s.maxCoins([3, 1, 5, 8])