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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self._result = []
        self.sum_path(root, sum, [])
        return self._result

    def sum_path(self, node, target, path_lst):
        if not node.left and not node.right and sum(path_lst) + node.val == target:
            path_lst.append(node.val)
            self._result.append(path_lst)
            return
        path_lst.append(node.val)
        copy_path = path_lst[:]
        if node.left:
            self.sum_path(node.left, target, copy_path)
        copy_path = path_lst[:]
        if node.right:
            self.sum_path(node.right, target, copy_path)

if __name__ == "__main__":
    head = generate_tree([1,2,3,4,5,6,7,8,9])
    s = Solution()
    print s.pathSum(head, 10)