class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        matrix = [[1 for i in range(m)] for j in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        print matrix[n-1][m-1]
    def unipath2(self, m, n):
        num = reduce(lambda x, y: x * y, range(1, m + n - 1))
        num1 = reduce(lambda x, y: x * y, range(1, m))
        num2 = reduce(lambda x, y: x * y, range(1, n))
        print num / (num1 * num2)

if __name__ == "__main__":
    s = Solution()
    s.uniquePaths(7, 3)
    s.unipath2(7, 3)