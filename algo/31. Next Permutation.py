class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        for pos in range(len_nums-2, -1, -1):
            if nums[pos] < nums[pos+1]:
                for i in range(len_nums-1, pos, -1):
                    if nums[i] > nums[pos]:
                        tmp = nums[i]
                        nums[i] = nums[pos]
                        nums[pos] = tmp
                        break
                left = pos + 1
                right = len_nums - 1
                while left < right:
                    tmp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = tmp
                    left += 1
                    right -= 1
                return

        left = 0
        right = len_nums - 1
        while left < right:
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left += 1
            right -= 1

if __name__ == "__main__":
    s = Solution()
    a = [1,2,7,4,3,1]
    b = [6,5,4]
    s.nextPermutation(b)
    print b