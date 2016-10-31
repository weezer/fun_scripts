class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        output_stack = []
        for i in range(n):
            print self.putqueue([i])

    def putqueue(self, Qstack):
        put_Q = len(Qstack)
        if put_Q < self.n:
            for i in range(self.n):
                flag = True
                for k, v in enumerate(Qstack):
                    if abs(put_Q - k) == abs(i - v) or v == i:
                        flag = False
                        break
                if flag:
                    nextStack = Qstack[:]
                    nextStack.append(i)
                    self.putqueue(nextStack)
        else:
            # print Qstack
            return Qstack


if __name__ == "__main__":
    s = Solution()
    s.solveNQueens(4)