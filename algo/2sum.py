class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        count = 0
        for i in nums:
            if hash_map.get(target - i) is not None:
                return [hash_map[target - i], count]
            hash_map[i] = count
            count += 1

        return [-1, -1]

if __name__ == "__main__":
    s = Solution()
    print s.twoSum([3, 3], 6)