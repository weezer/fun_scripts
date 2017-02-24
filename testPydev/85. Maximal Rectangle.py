lst = [[1, 0, 1, 0, 0],
       [1, 0, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 0, 0, 1, 0]]

lst = ["11111111","11111110","11111110","11111000","01111000"]

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        largest = 0
        my_matrix = []
        for i in matrix:
            my_matrix.append(map(int, list(i)))
        matrix = my_matrix
        print matrix
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] = matrix[i-1][j] + 1
        print matrix
        for i in matrix:
            largest = max(largest, self.largestRectangleArea(i))
        return largest

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        dummy_stack = heights[:] + [0]
        stack = []
        largest = 0
        pos = 0
        while pos < len(dummy_stack):
            if not stack or dummy_stack[pos] > dummy_stack[stack[-1]]:
                stack.append(pos)
                pos += 1
            else:
                cur_pos = stack.pop()
                largest = max(largest, dummy_stack[cur_pos] * (not stack and pos or pos - stack[-1] - 1))
        return largest


if __name__ == "__main__":
    s = Solution()
    print s.maximalRectangle(lst)