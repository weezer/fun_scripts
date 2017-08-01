class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            num = int(str(x)[::-1])
            max_int = 1 << 31
            return (num, 0)[num > max_int]
        else:
            min_int = -1 << 31
            str_x = str(x)
            len_x = len(str_x)
            num = int(str_x[0] + str_x[len_x:0:-1])
            return (num, 0)[num < min_int]