class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(0, len(board), 3):
            for j in range(0, range(board), 3):
                for num in range(1, 10):
