class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n + 1)
        for i in range(1, n+1):
            dp[i] = sum([dp[i-pos-1] * dp[pos] for pos in range(i)])
        print dp[n]

if __name__ == "__main__":
    s = Solution()
    s.numTrees(2)