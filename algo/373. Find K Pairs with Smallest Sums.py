class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        import heapq
        hq = []
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        if k > len_nums1 * len_nums2:
            k = len_nums1 * len_nums2
        count = 0
        nums2_start = nums2[0]
        def sort_return(arr):
            ans = []
            while arr:
                ans.append(heapq.heappop(hq)[1])
            return ans[::-1]

        for i in nums1:
            for j in nums2:
                if hq and count >= k and -hq[0][0] < i + nums2_start:
                    return sort_return(hq)[:k]
                else:
                    print hq
                    if count < k:
                        heapq.heappush(hq, (-(i + j), [i, j]))
                    else:
                        heapq.heappushpop(hq, (-(i + j), [i, j]))
                count += 1
        return sort_return(hq)[:k]

if __name__ == "__main__":
    s = Solution()
    print s.kSmallestPairs([1,2,3], [3,4,5], 4)