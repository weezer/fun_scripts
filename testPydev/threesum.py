class Solution(object):
    def permutation(self, nums):
        result = []
        import itertools
        for i in itertools.combinations(nums, 3):
            if sum(i) == 0:
                if sorted(list(i)) not in result:
                    result.append(sorted(list(i)))
        return result


    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        if len(nums) < 3:
            return result

        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i-1]:
                left = i + 1
                right = len(nums) - 1
            else:
                continue
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    right -= 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                else:
                    if nums[i] + nums[left] + nums[right] < 0:
                        left += 1
                    else:
                        right -= 1
        return result

if __name__ == "__main__":
    q = [-2, 0, 0 ,2 ,2]
    q1 = [0,4,5,1,1,-9,8,3,-1,-2,-3,2,1,9,-9,-6,4,1]
    q2 = [-2, -1, -1, 0, 2]
    q3 = [3,0,-2,-1,1,2]
    q4 = [3,2,1,0,-1,-2,-3]

    q5 = [-15,13,6,-11,-4,5,-13,5,3,2,6,-1,4,12,-10,-13,-7,-4,-5,6,9,-14,1,-6,13,7,-8,10,-4,11,-8,-3,1,5,-7,4,-13,-13,-5,-3,4,-14,11,-14,5,-13,-12,13,-10,-10,-4,-15,13,13,-14,11,-3,-15,6,1,3,5,13,-11,-5,-9,1,-2,-14,11,10,5,4,-1,6,-6,-7,9,-15,-2,7,-12,-10,5,-14,13,-6,-9,6,7,7,-6,-2,-3,-9,0,-5,7,5,-4,-5,-7,-13,14,7,8,-15,7,-5,-15,-10,9]
    q6 = [-1,0,1,2,-1,-4]
    q7 = [3,0,-2,-1,1,2]
    q8 = [0,-4,-1,-4,-2,-3,2]
    q9 = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    q10 = [0,1,0,0]
    q11 = [-2,0,1,1,2]
    q12 = [-1,0,1,2,-1,-4]
    q13 = [1,-1,-1,0]
    s = Solution()
    # print s.threeSum(q11)
    print s.permutation(q13)