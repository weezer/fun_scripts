# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.path_stack = []

        def dfs(root, stack):
            stack.append(root.val)
            if root.left is None and root.right is None:
                self.path_stack.append(stack)
            copy_stack = stack[:]
            if root.left:
                dfs(root.left, copy_stack)
            copy_stack = stack[:]
            if root.right:
                dfs(root.right, copy_stack)

        dfs(root, [])
        result = 0
        print self.path_stack
        for i in self.path_stack:
            multipler = 1
            j_result = 0
            while i:
                j = i.pop()
                j_result += multipler * j
                multipler *= 10
            result += j_result

        return result



