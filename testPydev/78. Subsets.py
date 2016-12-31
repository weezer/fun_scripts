class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for i in nums:
            for j in ans[:]:
                x = j[:]
                x.append(i)
                ans.append(x)
        return ans


if __name__ == "__main__":
    s = Solution()
    print s.subsets(range(5))