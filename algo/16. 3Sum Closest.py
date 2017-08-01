class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sorted_nums = sorted(nums)
        len_nums = len(nums)
        answer = 1 << 31
        for left in range(0, len_nums-2):
            if left > 0 and sorted_nums[left] == sorted_nums[left - 1]:
                continue
            mid = left + 1
            right = len_nums - 1
            while mid < right:
                if sorted_nums[left] + sorted_nums[mid] + sorted_nums[right] == target:
                    return target
                elif sorted_nums[left] + sorted_nums[mid] + sorted_nums[right] < target:
                    gap = abs(sorted_nums[left] + sorted_nums[mid] + sorted_nums[right] - target)
                    answer = (sorted_nums[left] + sorted_nums[mid] + sorted_nums[right], answer)[gap > abs(answer - target)]
                    mid += 1
                    while mid < right and sorted_nums[mid] == sorted_nums[mid-1]:
                        mid += 1
                else:
                    gap = abs(sorted_nums[left] + sorted_nums[mid] + sorted_nums[right] - target)
                    answer = (sorted_nums[left] + sorted_nums[mid] + sorted_nums[right], answer)[
                        gap > abs(answer - target)]
                    right -= 1
                    while mid < right and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1
        return answer

if __name__ == "__main__":
    s = Solution()
    print s.threeSumClosest([1,1,1,0], -100)