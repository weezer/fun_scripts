class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

    def findKth(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])

        if (len(A) / 2 + len(B) / 2) < k:
            if A[len(A) / 2] < B[len(B) / 2]:
                return self.findKth(A[(len(A)+1)/2:], B, k - ((len(A) + 1)/2))
            else:
                return self.findKth(A, B[(len(B)+1) / 2:], k - ((len(B) +1)/ 2))
        else:
            if A[len(A) / 2] < B[len(B) / 2]:
                return self.findKth(A, B[:len(B)/2], k)
            else:
                return self.findKth(A[:len(A)/2], B, k)


if __name__ == "__main__":
    s = Solution()
    print s.findKth([1,2,3,4,5,6], [11,12,13], 5)