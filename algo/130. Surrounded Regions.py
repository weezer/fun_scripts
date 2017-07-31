class Solution(object):

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def find(the_pos):
            if solve_matrix[the_pos] != the_pos:
                return find(solve_matrix[the_pos])
            return the_pos

        def union():
            if solve_matrix[pos] == 0:
                if solve_matrix[pos - gap] != 0:
                    solve_matrix[pos] = find(pos - gap)
                if solve_matrix[pos] == 0 and solve_matrix[pos - 1] != 0:
                    solve_matrix[pos] = find(pos - 1)
                elif solve_matrix != 0 and solve_matrix[pos - 1] != 0:
                    solve_matrix[find(pos - 1)] = solve_matrix[pos]
                elif solve_matrix[pos] == 0:
                    solve_matrix[pos] = pos
            else:
                if pos > gap and solve_matrix[pos - gap] != 0:
                    solve_matrix[find(pos - gap)] = pos
                if pos % gap > 1 and solve_matrix[pos - 1] != 0:
                    solve_matrix[find(pos - 1)] = pos

        x_axis = len(board)
        y_axis = len(board[0])
        gap = y_axis
        solve_matrix = [0] + [0 for i in range(y_axis * x_axis)]
        for i in range(x_axis):
            for j in range(1, y_axis+1):
                if board[i][j-1] == "O":
                    pos = i * y_axis + j
                    if i == 0 or i == x_axis - 1 or j == 1 or j == y_axis:
                        solve_matrix[pos] = pos
                    union()
                    print solve_matrix

        print solve_matrix

if __name__ == "__main__":
    case1 = ["XXXX","XOOX","XXOX","XOOX","XOXX"]
    s = Solution()
    s.solve(case1)