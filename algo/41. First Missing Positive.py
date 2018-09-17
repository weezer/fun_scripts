class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        kv = {}
        kv[0] = 0
        for i in nums:
            if i > 0:
                if kv.get(i) is not None:
                    continue
                kv[i] = i
                if kv.get(i-1) is not None:
                    kv[i] = kv[i-1]
                    kv[kv[i]] = i
                if kv.get(i+1):
                    position = kv[i]
                    kv[kv[i]] = kv[i+1]
                    kv[kv[i+1]] = position
            print kv

    def anotherMethod(self, nums):
        len_nums = len(nums)
        for i in nums:
            position = i
            while len_nums >= position > 0 and position != nums[position-1]:
                tmp = nums[position-1]
                nums[position-1] = position
                position = tmp
        print nums
        for i in range(1, len_nums+1):
            if nums[i-1] != i:
                return i

        return i+1




if __name__ == "__main__":
    s = Solution()
    print s.anotherMethod([1,2,0])

