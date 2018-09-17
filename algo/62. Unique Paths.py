class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dividend = self.factorial(m + n - 2)
        divisor = self.factorial(m-1)
        divisor *= self.factorial(n-1)
        return dividend / divisor

    def factorial(self, m):
        result = 1
        for i in range(1, m + 1):
            result *= i
        return result

if __name__ == "__main__":
    s = Solution()
    print s.uniquePaths(3,7)