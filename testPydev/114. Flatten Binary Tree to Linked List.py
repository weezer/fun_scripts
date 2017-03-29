class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        _stack = []
        def pre_order(node, stack):
            stack.append(node)
            if node.left:
                pre_order(node.left, stack)
            if node.right:
                pre_order(node.right, stack)
        pre_order(root, _stack)
        head = root
        for i in _stack[1:]:
            root.right = i
            root.left = None
            root = root.right
        return head

if __name__ == "__main__":
    head = generate_tree([1,2,3,4,5,6,7,8,9])
    s = Solution()
    head = s.flatten(head)

    while head:
        print head.val
        head = head.right
