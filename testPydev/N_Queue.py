class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.collect = []
        output_stack = []
        for i in range(n):
            self.putqueue([i])
        print len(self.collect)
        for i in self.collect:
            ret_matrix = self.generatgraphic(i)
            output_stack.append(ret_matrix[:])
        return output_stack

    def generatgraphic(self, lst):
        dotmatrix = []
        for i in lst:
            dotline = ["." for x in range(self.n)]
            dotline[i] = "Q"
            dotline = "".join(dotline)
            dotmatrix.append(dotline[:])
        ",".join(dotmatrix)
        return dotmatrix

    def putqueue(self, qstack):
        put_Q = len(qstack)
        if put_Q < self.n:
            for i in range(self.n):
                flag = True
                for k, v in enumerate(qstack):
                    if abs(put_Q - k) == abs(i - v) or v == i:
                        flag = False
                        break
                if flag:
                    nextstack = qstack[:]
                    nextstack.append(i)
                    self.putqueue(nextstack)
        else:
            self.collect.append(qstack[:])

if __name__ == "__main__":
    s = Solution()
    print s.solveNQueens(5)