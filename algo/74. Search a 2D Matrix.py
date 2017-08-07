class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        upper = len(matrix) - 1
        if upper < 0:
            return False
        lower = 0
        left = 0
        right = len(matrix[0]) - 1
        if right < 0 or matrix[upper][right] < target or target < matrix[0][0]:
            return False

        def find_row(lower, upper):
            while lower <= upper:
                mid = (lower + upper) / 2
                if matrix[mid][0] == target:
                    return mid
                elif matrix[mid][0] < target and mid == len(matrix) - 1 or matrix[mid][0] < target < matrix[mid + 1][0]:
                    return mid
                elif matrix[mid][0] < target:
                    lower = mid + 1
                else:
                    upper = mid - 1

        row_number = find_row(lower, upper)

        def find_number(left, right):
            print row_number
            while left <= right:
                mid = (left + right) / 2
                if matrix[row_number][mid] == target:
                    return True
                elif matrix[row_number][left] == target:
                    return True
                elif matrix[row_number][right] == target:
                    return True
                elif matrix[row_number][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        return find_number(left, right)


if __name__ == "__main__":
    s = Solution()
    # print s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3)
    # print s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 24)
    print s.searchMatrix([[1]], 1)

