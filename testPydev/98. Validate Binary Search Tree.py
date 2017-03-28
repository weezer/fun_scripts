# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []

        def inorder(root, stack):
            if root.left:
                inorder(root.left, stack)
            stack.append(root.val)
            if root.right:
                inorder(root.right, stack)
        inorder(root, stack)

        return sorted(stack) == stack and len(set(stack)) == len(stack)


if __name__ == "__main__":
    root = TreeNode(5)
    head = root
    root.left = TreeNode(3)
    root = root.left
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root = head
    root.right = TreeNode(7)
    root = root.right
    root.right = TreeNode(2)

    s = Solution()
    print s.isValidBST(head)