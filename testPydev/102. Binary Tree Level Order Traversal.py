# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        import collections
        current_level = collections.deque()
        current_level.append(root)
        return_answer = []
        while current_level:
            return_answer.append(list(x.val for x in current_level))
            current_level_len = len(current_level)
            for i in range(current_level_len):
                current_node = current_level.popleft()
                if current_node.left:
                    current_level.append(current_node.left)
                if current_node.right:
                    current_level.append(current_node.right)
        return return_answer

if __name__ == "__main__":
    root = TreeNode(6)
    head = root
    root.left = TreeNode(3)
    root = root.left
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root = head
    root.right = TreeNode(7)
    root = root.right
    root.left = TreeNode(8)
    root.right = TreeNode(10)
    root = root.right
    root.left = TreeNode(9)
    root.right = TreeNode(11)

    s = Solution()
    print s.levelOrder(head)