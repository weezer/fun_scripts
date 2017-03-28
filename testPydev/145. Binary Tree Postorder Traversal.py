# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        import collections
        return_queue = collections.deque()
        stack = []
        if not root:
            return stack
        else:
            stack.append(root)
        while stack:
            current = stack.pop()
            return_queue.appendleft(current.val)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        print return_queue

def generate_tree(nums):
    import collections
    q = collections.deque()
    q.extend(nums)
    node_queue = collections.deque()
    head_node = TreeNode(q.popleft())
    node_queue.append(head_node)
    while node_queue:
        current = node_queue.popleft()
        if not current:
            continue
        if not q:
            break
        v1 = q.popleft()
        if v1 is not "#":
            left = TreeNode(v1)
            current.left = left
            node_queue.append(left)
        v2 = q.popleft()
        if v2 is not "#":
            right = TreeNode(v2)
            current.right = right
            node_queue.append(right)
    return head_node


def inorder(root):
    if root.left:
        inorder(root.left)
    print root.val
    if root.right:
        inorder(root.right)


if __name__ == "__main__":
    root = TreeNode(6)
    head = root
    root.left = TreeNode(3)
    root = root.left
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root = head
    root.right = TreeNode(8)
    root = root.right
    root.left = TreeNode(7)
    root.right = TreeNode(10)
    root = root.right
    root.left = TreeNode(9)
    root.right = TreeNode(11)
    # inorder(head)
    # s = Solution()
    # s.postorderTraversal(head)
    head = generate_tree([1,2,3,"#", "#",5,6,7,8])
    inorder(head)