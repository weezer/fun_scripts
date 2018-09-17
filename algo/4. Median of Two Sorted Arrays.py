# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         len_nums1 = len(nums1)
#         len_nums2 = len(nums2)
#         if (len_nums1 + len_nums2) % 2 == 1:
#             return self.findKthLargestNumber(nums1, nums2, (len_nums2 + len_nums1) / 2 + 1)
#         else:
#             small = self.findKthLargestNumber(nums1, nums2, (len_nums2 + len_nums1) / 2)
#             large = self.findKthLargestNumber(nums1, nums2, (len_nums2 + len_nums1) / 2 + 1)
#             return (small + large) / 2.0
#
#     def findKthLargestNumber(self, nums1, nums2, k):
#         nums1_len = len(nums1)
#         nums2_len = len(nums2)
#         if nums1_len == 0:
#             return nums2[k-1]
#         if nums2_len == 0:
#             return nums1[k-1]
#         if k == 1:
#             return min(nums1[0], nums2[0])
#         if k/2 > nums2_len or (k/2 <= nums1_len and nums1[k/2 - 1] < nums2[k/2 - 1]):
#             return self.findKthLargestNumber(nums1[k/2:], nums2, k - k/2)
#         else:
#             return self.findKthLargestNumber(nums1, nums2[k/2:], k - k/2)


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        if (len_nums1 + len_nums2) % 2:
            return self.find_k_in_array(nums1, nums2, (len_nums1 + len_nums2) / 2)
        else:
            return (self.find_k_in_array(nums1, nums2, (len_nums1 + len_nums2) / 2) + self.find_k_in_array(nums1, nums2,
                                                                                                           (
                                                                                                           len_nums1 + len_nums2) / 2 + 1)) / 2.0

    def find_k_in_array(self, nums1, nums2, k):
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        if len_nums1 == 0:
            return nums2[k - 1]
        if len_nums2 == 0:
            return nums1[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        if len_nums2 < k / 2 or (len_nums1 >= k / 2 and (nums1[k / 2 - 1] < nums2[k / 2 - 1])):
            return self.find_k_in_array(nums1[k / 2:], nums2, k - k / 2)
        else:
            return self.find_k_in_array(nums1, nums2[k / 2:], k - k / 2)

s = Solution()
print s.findMedianSortedArrays([2,3,4,5,6], [1])



