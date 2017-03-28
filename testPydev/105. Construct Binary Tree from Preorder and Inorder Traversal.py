# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder and not inorder:
            return None
        root = TreeNode(preorder[0])
        root_pos_inorder = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:root_pos_inorder+1], inorder[:root_pos_inorder])
        root.right = self.buildTree(preorder[root_pos_inorder+1:], inorder[root_pos_inorder+1:])
        # print root.val
        return root

    def inorder_traversal(self, root):
        if not root:
            return
        if root.left:
            self.inorder_traversal(root.left)
        print root.val
        if root.right:
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if not root:
            return
        print root.val
        if root.left:
            self.preorder_traversal(root.left)
        if root.right:
            self.preorder_traversal(root.right)

if __name__ == "__main__":
    s = Solution()
    head = s.buildTree([6,4,3,5,8,7,9], [3,4,5,6,7,8,9])
    # print head.val
    s.inorder_traversal(head)
    s.preorder_traversal(head)