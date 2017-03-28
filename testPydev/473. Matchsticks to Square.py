class Solution(object):
    def makesquare(self, nums):
        if not nums:
            return False
        sumn = sum(nums)
        nums.sort(reverse=True)
        if sumn % 4:
            return False
        return self.dfs(nums, [0, 0, 0, 0], 0, sumn / 4)




if __name__ == "__main__":
    L1 = [10, 6, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2]
    L2 = [2,2,2,3,4,4,4,5,6]
    L3 = [2,2,2,2,2,6]
    L4 = [1, 1, 1, 1]
    L5 = []
    L6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 32, 4, 32, 2, 34, 4, 3, 43, 43, 2, 2, 34, 43, 2, 34, 43, 2, 34, 43, 24, 3, 24,
           32, 3, 21, 64, 6, 5, 5, 3]
    L7 = [2,2,2,2,2,2]
    L8 = [6,6,6,6,6,6]
    L9 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    L10 = [5,5,5,5,4,4,4,4,3,3,3,3]
    L11 = [2,2,2,1,1]

    s = Solution()
    print s.makesquare(L10)