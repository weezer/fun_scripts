# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return None
        def dfs(node):
            if not node:
                return 0
            else:
                return max(dfs(node.left), dfs(node.right)) + 1

        lt = dfs(root.left)
        rt = dfs(root.right)
        if abs(lt - rt) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)