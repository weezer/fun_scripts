# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, A, B):
        if root is None:
            return None

        if root is A or root is B:
            return root

        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)

        if left is not None and right is not None:
            return root
        if left is not None:
            return left
        if right is not None:
            return right
        return None

if __name__ == "__main__":
    root = TreeNode(6)
    head = root
    root.left = TreeNode(3)
    node1 = root.left
    root = root.left
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root = head
    root.right = TreeNode(8)
    root = root.right
    root.left = TreeNode(7)
    node2 = root.left
    root.right = TreeNode(10)
    root = root.right
    root.left = TreeNode(9)
    root.right = TreeNode(11)

    s = Solution()
    print s.lowestCommonAncestor(head, node1, TreeNode(123)).val
