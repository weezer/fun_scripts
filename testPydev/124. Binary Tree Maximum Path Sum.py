# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        def helper(node):
            if not node:
                return -1 << 31, 0
            left_sum = helper(node.left)
            right_sum = helper(node.right)
            total_sum = max(left_sum[1] + right_sum[1] + node.val, left_sum[0], right_sum[0])
            single_sum = max(max(left_sum[1], right_sum[1]) + node.val, 0)
            return total_sum, single_sum

        result = helper(root)
        return result[0]


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

if __name__ == "__main__":
    head = generate_tree([1,-2,-3,1,3,-2,"#",-1, "#", "#", "#", "#", "#", "#", "#"])
    s = Solution()
    print s.maxPathSum(head)

