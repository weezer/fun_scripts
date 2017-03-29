class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        stack = []
        for i in range(numRows):
            temp_stack = []
            for j in range(i):
                temp_stack.append(stack[i-1][j-1] + stack[i-1][j])
            temp_stack.append(1)
            stack.append(temp_stack)
        return stack

if __name__ == "__main__":
    s = Solution()
    print s.generate(3)