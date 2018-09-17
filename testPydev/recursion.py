class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        self.dfs(ans, 0, 0, n, [])
        return ["".join(i) for i in ans]

    def dfs(self, answer, l_n, r_n, n, tmp):
        if len(tmp) == n * 2:
            answer.append(tmp)
            return
        if l_n < n:
            self.dfs(answer, l_n + 1, r_n, n, tmp[:] + ["("])
        if r_n < l_n:
            self.dfs(answer, l_n, r_n+1, n, tmp[:] + [")"])

if __name__ == "__main__":
    s = Solution()
    print s.generateParenthesis(3)