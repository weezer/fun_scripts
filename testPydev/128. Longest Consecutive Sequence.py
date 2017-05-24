class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        kv = {}
        for i in nums:
            #
            # print i
            if kv.get(i) is not None:
                continue
            kv[i] = i
            low = kv.get(i-1, i)
            high = kv.get(i+1, i)
            kv[low] = high
            kv[high] = low
            # print kv
        max_gap = 0
        # print kv
        for k, v in kv.items():
            max_gap = max(abs(k-v), max_gap)
        return max_gap+1


if __name__ == "__main__":
    s = Solution()
    print s.longestConsecutive([-4,-1,4,-5,1,-6,9,-6,0,2,2,7,0,9,-3,8,9,-2,-6,5,0,3,4,-2])
    print sorted([-4,-1,4,-5,1,-6,9,-6,0,2,2,7,0,9,-3,8,9,-2,-6,5,0,3,4,-2])