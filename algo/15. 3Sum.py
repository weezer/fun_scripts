class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        len_nums = len(nums)
        r_answer = []
        sorted_nums = sorted(nums)
        for left in range(len_nums-2):
            if left > 0 and sorted_nums[left] == sorted_nums[left - 1]:
                continue
            mid = left + 1
            right = len_nums - 1
            while mid < right:
                if sorted_nums[mid] + sorted_nums[right] == -sorted_nums[left]:
                    r_answer.append([sorted_nums[left], sorted_nums[mid], sorted_nums[right]])
                    mid += 1
                    while sorted_nums[mid] == sorted_nums[mid - 1] and mid < right:
                        mid += 1
                    right -= 1
                    while sorted_nums[right] == sorted_nums[right + 1] and mid < right:
                        right -= 1
                elif sorted_nums[mid] > -sorted_nums[left]:
                    break
                elif sorted_nums[mid] + sorted_nums[right] < -sorted_nums[left]:
                    mid += 1
                    while sorted_nums[mid] == sorted_nums[mid - 1] and mid < right:
                        mid += 1
                elif sorted_nums[mid] + sorted_nums[right] > -sorted_nums[left]:
                    right -= 1
                    while sorted_nums[right] == sorted_nums[right + 1] and mid < right:
                        right -= 1
        return r_answer
    
if __name__ == "__main__":
    s = Solution()
    print s.threeSum([-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0])
