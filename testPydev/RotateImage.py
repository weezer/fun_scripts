class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        newMatrix = [[0 for x in range(len(matrix))] for y in range(len(matrix))]

        n = len(matrix) - 1
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                newMatrix[j][n] = matrix[i][j]
            n -= 1

        return newMatrix


    def inplacerotate(self, matrix):
        n = len(matrix) - 1
        for i in range(len(matrix)/2):
            tmp = matrix[i]
            matrix[i] = matrix[n - i]
            matrix[n - i] = tmp

        n = 1
        for i in range(len(matrix)):
            for j in range(n, len(matrix)):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
            n += 1

        print matrix

if __name__ == "__main__":
    s = Solution()
    s.inplacerotate([[1,2,3], [4,5,6], [7,8,9]])
    s.inplacerotate([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
    s.inplacerotate([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])