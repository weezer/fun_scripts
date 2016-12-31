matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """



def binary_search(lst, target):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) / 2
        if lst[mid] == target:
            return True
        if lst[mid] > target:
            end = mid - 1
        if lst[mid] < target:
            start = mid + 1
    return False


a = [1,3,5,7,9]
for i in range(11):
    print i , binary_search(a, i)