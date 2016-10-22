class Solution(object):
    def combinationSum(self, nums, target):
        self.result = []
        self.combinationMethod([], nums, target)
        return self.result

    def combinationMethod(self, current_nums, nums, target):
        for i in range(len(nums)):
            if sum(current_nums) + nums[i] == target:
                answer_nums = current_nums[:]
                answer_nums.append(nums[i])
                if answer_nums.sort() not in self.result:
                    self.result.append(answer_nums)
            if sum(current_nums) + nums[i] < target:
                remain_nums = nums[i+1:]
                answer_nums = current_nums[:]
                answer_nums.append(nums[i])
                self.combinationMethod(answer_nums, remain_nums, target)


if  __name__ == "__main__":
    s = Solution()
    print s.combinationSum([10,1,2,7,6,1,5], 8)