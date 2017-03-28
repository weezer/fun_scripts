class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lst = [[]]
        nums.sort()
        for i in nums:
            len_lst = len(lst)
            for j in xrange(len_lst):
                element_copy = lst[j][:]
                element_copy.append(i)
                if element_copy not in lst:
                    lst.append(element_copy)
        return lst


if __name__ == "__main__":
    s = Solution()
    print s.subsetsWithDup([1,2,3])