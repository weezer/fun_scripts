# Complete the function below.
import operator


def dfs(grid_matrix, i, j):
    if i > len(grid_matrix) - 1 or i < 0 or j > len(grid_matrix[0]) - 1 or j < 0:
        return
    if grid_matrix[i][j] == 'N':
        return
    grid_matrix[i][j] = 'N'
    dfs(grid_matrix, i + 1, j)
    dfs(grid_matrix, i, j + 1)
    dfs(grid_matrix, i - 1, j)
    dfs(grid_matrix, i, j - 1)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def combinations(n, r):
    numerator = factorial(n)
    denominator = factorial(r) * factorial(n - r)
    return int(numerator / denominator)


def combi(n, k, dp):

    for i in range(1, n + 1):
        j = min(i, k)
        while (j > 0):
            dp[j] = dp[j] + dp[j - 1]
            j -= 1
    print dp
    return dp[k]

def Group(grid):
    ans = 0
    grid_matrix = [list(x) for x in grid]
    print grid_matrix
    if not len(grid_matrix):
        ans = 0
    else:
        m = len(grid_matrix)
        n = len(grid_matrix[0])
        for i in range(m):
            for j in range(n):
                if grid_matrix[i][j] == 'Y':
                    dfs(grid_matrix, i, j)
                    ans += 1
    ans = 15
    dp = [0 for i in xrange(ans + 1)]
    dp[0] = 1
    count = 0
    for i in range(0, ans, 2):
        count += combi(ans, i, dp)
    return count


if __name__ == '__main__':
    print Group(["YNNY", "NYNY", "NYNN"])
