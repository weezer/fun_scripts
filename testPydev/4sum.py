class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result_set = []
        if len(nums) < 4:
            return result_set
        nums.sort()
        print nums
        for i in range(len(nums) - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    if target == nums[i] + nums[j] + nums[left] + nums[right]:
                        print i, j, left, right
                        result_set.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[right + 1] == nums[right]:
                            right -= 1
                        while left < right and nums[left - 1] == nums[left]:
                            left += 1
                    if target < nums[i] + nums[j] + nums[left] + nums[right]:
                        right -= 1
                        while left < right and nums[right + 1] == nums[right]:
                            right -= 1
                    if target > nums[i] + nums[j] + nums[left] + nums[right]:
                        left += 1
                        while left < right and nums[left - 1] == nums[left]:
                            left += 1

        return result_set


if __name__ == "__main__":
    s = Solution()
    print s.fourSum([-1,0,-5,-2,-2,-4,0,1,-2], -9)