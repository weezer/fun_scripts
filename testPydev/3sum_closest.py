class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0

        nums.sort()
        least_diff = nums[0] + nums[1] + nums[len(nums)-1] - target
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                left = i + 1
                right = len(nums) - 1
            else:
                continue
            while left < right:
                if nums[i] + nums[left] + nums[right] == target:
                    return target
                if target < nums[i] + nums[left] + nums[right]:
                    least_diff = (least_diff, nums[i] + nums[left] + nums[right] - target)[abs(nums[i] + nums[left] +
                                                                                               nums[right] - target)
                                                                                           < abs(least_diff)]
                    right -= 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1
                if target > nums[i] + nums[left] + nums[right]:
                    least_diff = (least_diff, nums[i] + nums[left] + nums[right] - target)[abs(nums[i] + nums[left] +
                                                                                               nums[right] - target)
                                                                                           < abs(least_diff)]
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return least_diff + target


if __name__ == "__main__":
    lst1 = [1,1,1,0]
    num1 = -100
    lst2 = [1, 2, 4, 8, 16, 32, 64, 128]
    num2 = 82
    lst3 = [-10, 0, -2, 3, -8, 1, -10, 8, -8, 6, -7, 0, -7, 2, 2, -5, -8, 1, -4, 6]
    num3 = 18
    s = Solution()
    print s.threeSumClosest(lst2, num2)