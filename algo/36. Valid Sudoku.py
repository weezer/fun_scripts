class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        row = [set() for i in range(len(board))]
        col = [set() for i in range(len(board))]
        cube = [set() for i in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board)):
                number = board[i][j]
                if number == '.':
                    continue
                if number in row[i]:
                    return False
                if number in col[j]:
                    return False

                cube_index = i/3*3 + j/3
                if number in cube[cube_index]:
                    return False

                row[i].add(number)
                col[j].add(number)
                cube[cube_index].add(number)
        return True