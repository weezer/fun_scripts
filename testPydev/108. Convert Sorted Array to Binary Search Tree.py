# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        nums_len = len(nums)
        if nums_len == 0:
            return None
        root = TreeNode(nums[nums_len/2])
        root.left = self.sortedArrayToBST(nums[:nums_len/2])
        root.right = self.sortedArrayToBST(nums[(nums_len/2)+1:])
        return root

    def inorder(self, root):
        if root.left:
            self.inorder(root.left)
        print root.val
        if root.right:
            self.inorder(root.right)


if __name__ == "__main__":
    s = Solution()
    head = s.sortedArrayToBST([1,2,3,4,5,6,7,8])
    s.inorder(head)