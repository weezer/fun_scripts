class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = {}
        for i in nums:
            if k.get(i) >= 2:
                continue
            elif k.get(i):
                k[i] += 1
            else:
                k[i] = 1
        print k
        k.keys().sort

        print int(''.join([(str(i) * k[i]) for i in k.keys()]))

if __name__ == "__main__":
    s = Solution()
    s.removeDuplicates([1,1,1,2,3])