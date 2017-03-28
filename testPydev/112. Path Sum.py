# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        self.check = False
        def dfs(node, path_lst):
            print path_lst
            if not node.left and not node.right:
                result = node.val
                for i in path_lst:
                    result += i
                if result == sum:
                    self.check = True
                    return
            path_lst.append(node.val)
            copy_path_lst = path_lst[:]
            if node.left:
                dfs(node.left, copy_path_lst)
            copy_path_lst = path_lst[:]
            if node.right:
                dfs(node.right, copy_path_lst)
        dfs(root, [])

        return self.check