

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.word = word
        self.col = len(board[0])
        self.row = len(board)
        self.flag = False
        # arrived = [[0 for i in range(self.col)] for j in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                if board[i][j] == word[0]:
                    rest_word = word[1:]
                    arrived = [[0 for x in range(self.col)] for y in range(self.row)]
                    self.find_word(i, j, arrived, rest_word)
                if self.flag:
                    return self.flag
        return self.flag

    def find_word(self, row_num, col_num, arrived_matrix, rest_word):
        if len(rest_word) == 0:
            self.flag = True
            return
        arrived_matrix = [x[:] for x in arrived_matrix]
        arrived_matrix[row_num][col_num] = 1
        the_word = rest_word[:]
        print the_word
        print arrived_matrix
        if row_num-1 >= 0 and arrived_matrix[row_num-1][col_num] != 1 and the_word[0] == self.board[row_num-1][col_num]:
            self.find_word(row_num - 1, col_num, arrived_matrix[:], the_word[1:])
        if row_num+1 < self.row and arrived_matrix[row_num+1][col_num] != 1 and the_word[0] == self.board[row_num+1][
                    col_num]:
            self.find_word(row_num + 1, col_num, arrived_matrix[:], the_word[1:])
        if col_num-1 >= 0 and arrived_matrix[row_num][col_num-1] != 1 and the_word[0] == self.board[row_num][col_num-1]:
            self.find_word(row_num, col_num - 1, arrived_matrix[:], the_word[1:])
        if col_num+1 < self.col and arrived_matrix[row_num][col_num+1] != 1 and the_word[0] == self.board[row_num][
                    col_num+1]:
            self.find_word(row_num, col_num + 1, arrived_matrix[:], the_word[1:])
        if self.flag == True:
            return True
        else:
            return False

if __name__ == "__main__":
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    b_a = 'ABCESCFSADEE'

    b1 = [['C', 'A', 'A'], ['A', 'A', 'D'], ['B', 'C', 'D']]
    a = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaab"]
    input_a = [list(x) for x in a]
    print input_a
    b = "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    s = Solution()
    print s.exist(board, b_a)
