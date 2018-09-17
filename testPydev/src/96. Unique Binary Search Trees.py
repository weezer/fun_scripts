class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n + 1)
        for i in range(2, n+1):
            cal = 0
            for j in range(i):
                left = dp[j]
                right = dp[i-j-1]
                cal += left * right
            dp[i] = cal
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print s.numTrees(4)

