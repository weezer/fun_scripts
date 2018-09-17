class Solution(object):
    def jump2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        MAX_INT = 1 << 31
        jump_lst = [0] + [MAX_INT] * (len_nums - 1)
        for i in range(len_nums):
            jump_num = nums[i]
            for j in range(1, jump_num+1):
                if i + j < len_nums:
                    jump_lst[i+j] = min(jump_lst[i] + 1, jump_lst[i+j])
        print jump_lst

    def jump(self, nums):
        new_right = nums[0]
        step = 0
        pos = 0
        len_nums = len(nums)
        while pos < len_nums:
            step += 1
            right = new_right
            while pos <= right and pos < len_nums:
                new_right = max(pos + nums[pos], new_right)
                pos += 1
        return step

if __name__ == "__main__":
    s = Solution()
    print s.jump([1,2])
