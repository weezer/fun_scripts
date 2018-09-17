class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        for i in range(n):
            self.dfs([i], 1, n, ans)
        return ans

    def dfs(self, lst, row, n, ans):
        print lst
        if row == n:
            ans.append(lst)
        for i in range(n):
            if self.valid(lst, row, i):
                self.dfs(lst + [i], row+1, n, ans)

    def valid(self, lst, n_row, n_col):
        for x, y in enumerate(lst):
            if (x - y) == (n_row - n_col) or (x + y) == (n_row + n_col) or n_col == y:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print s.totalNQueens(4)