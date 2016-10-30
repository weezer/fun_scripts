class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """


    def findKth(self, A, B, k):
        if len(A) <= 0:
            return B[k - 1]
        if len(B) <= 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])

        if (len(A) + len(B))/2 + 1 > k:
            if A[len(A)/2] > B[len(B)/2]:
                return self.findKth(A[:len(A)/2], B, k)
            else:
                return self.findKth(A, B[:len(B)/2], k)
        else:
            if A[len(A) / 2] > B[len(B) / 2]:
                return self.findKth(A, B[len(B)/2 + 1:], k - len(B)/2 - 1)
            else:
                return self.findKth(A[len(A)/2 + 1:], B, k - len(A)/2 - 1)

if __name__ == "__main__":
    s = Solution()
    # for i in range(1, 10):
    # print s.findKth([1,2,3,7,8,9], [4,5,6], i)
    print s.findKth([1,2,3,4], [], 3)
        # print s.findKth([1,2,3,4,5,6], [7,8,9], i)
        # print ""