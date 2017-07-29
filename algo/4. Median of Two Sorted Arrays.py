class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        if (len_nums1 + len_nums2) % 2 == 1:
            return self.findKthLargestNumber(nums1, nums2, (len_nums2 + len_nums1) / 2 + 1)
        else:
            small = self.findKthLargestNumber(nums1, nums2, (len_nums2 + len_nums1) / 2)
            large = self.findKthLargestNumber(nums1, nums2, (len_nums2 + len_nums1) / 2 + 1)
            return (small + large) / 2.0

    def findKthLargestNumber(self, nums1, nums2, k):
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        if nums1_len == 0:
            return nums2[k-1]
        if nums2_len == 0:
            return nums1[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        if k/2 > nums2_len or (k/2 <= nums1_len and nums1[k/2 - 1] < nums2[k/2 - 1]):
            return self.findKthLargestNumber(nums1[k/2:], nums2, k - k/2)
        else:
            return self.findKthLargestNumber(nums1, nums2[k/2:], k - k/2)

s = Solution()



