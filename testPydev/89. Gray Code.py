class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        lst = ['0', '1']
        dummy_lst = []
        if n == 0:
            return 0
        if n == 1:
            return lst
        while n > 1:
            for i in lst:
                dummy_lst.append('0' + i)
            for i in lst[::-1]:
                dummy_lst.append('1' + i)
            lst = dummy_lst[:]
            dummy_lst = []
            n -= 1
        return map(lambda x: int(x, 2), lst)

if __name__ =="__main__":
    s = Solution()
    print s.grayCode(3)