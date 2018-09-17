class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for i in range(n)] for j in range(n)]
        self.count = 1
        self.n2 = pow(n, 2)
        self.write_into_matrix([0, 0], n, matrix)
        return matrix

    def write_into_matrix(self, pos, num, matrix):
        while self.count <= self.n2:

            if self.count <= self.n2:
                pos = self.move_right(pos, num, matrix)
            print matrix
            if self.count <= self.n2:
                pos = [pos[0] + 1, pos[1]]
                pos = self.move_down(pos, num-1, matrix)
            print matrix
            if self.count <= self.n2:
                pos = [pos[0], pos[1] - 1]
                pos = self.move_left(pos, num-1, matrix)
            print matrix
            if self.count <= self.n2:
                pos = [pos[0] - 1, pos[1]]
                pos = self.move_up(pos, num-2, matrix)
            print matrix
            pos = [pos[0], pos[1] + 1]
            num -= 2

    def move_right(self, pos, num, matrix):
        for i in range(num):
            matrix[pos[0]][pos[1] + i] = self.count
            self.count += 1
        return [pos[0], pos[0] + i]

    def move_down(self, pos, num, matrix):
        for i in range(num):
            matrix[pos[0] + i][pos[1]] = self.count
            self.count += 1
        return [pos[0] + i, pos[0] + i]

    def move_left(self, pos, nums, matrix):
        for i in range(nums):
            matrix[pos[0]][pos[1] - i] = self.count
            self.count += 1
        return [pos[0], pos[1] - i]

    def move_up(self, pos, nums, matrix):
        for i in range(nums):
            matrix[pos[0] - i][pos[1]] = self.count
            self.count += 1
        return [pos[0] - i, pos[1]]

if __name__ == "__main__":
    s = Solution()
    print s.generateMatrix(4)