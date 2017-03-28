# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder and not postorder:
            return None
        root = TreeNode(postorder[-1])
        root_pos_inorder = inorder.index(root.val)
        inorder_len = len(inorder)
        root.left = self.buildTree(inorder[:root_pos_inorder], postorder[:root_pos_inorder])
        root.right = self.buildTree(inorder[root_pos_inorder+1:], postorder[root_pos_inorder:-1])
        return root

    def inorder(self, root):
        if not root:
            return
        if root.left:
            self.inorder(root.left)
        print root.val
        if root.right:
            self.inorder(root.right)

    def postorder(self, root):
        if not root:
            return
        if root.left:
            self.postorder(root.left)
        if root.right:
            self.postorder(root.right)
        print root.val


if __name__ == "__main__":
    s = Solution()
    head = s.buildTree([1,2,3,4,5], [1,3,2,5,4])
    s.inorder(head)
    s.postorder(head)