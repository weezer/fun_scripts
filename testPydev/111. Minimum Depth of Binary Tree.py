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
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        import collections
        q = collections.deque()
        q.append(root)
        depth = 1
        while q:
            q_len = len(q)
            while q_len > 0:
                current_node = q.popleft()
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
                if not current_node.left and not current_node.right:
                    return depth
                q_len -= 1
            depth += 1


if __name__ == "__main__":
    head = generate_tree([1,2,3,4,5,6,7,8,9])
    s = Solution()
    print s.minDepth(head)