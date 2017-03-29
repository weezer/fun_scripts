# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def generate_tree(nums):
    import collections
    q = collections.deque()
    q.extend(nums)
    node_queue = collections.deque()
    head_node = TreeLinkNode(q.popleft())
    node_queue.append(head_node)
    while node_queue:
        current = node_queue.popleft()
        if not current:
            continue
        if not q:
            break
        v1 = q.popleft()
        if v1 is not "#":
            left = TreeLinkNode(v1)
            current.left = left
            node_queue.append(left)
        v2 = q.popleft()
        if v2 is not "#":
            right = TreeLinkNode(v2)
            current.right = right
            node_queue.append(right)
    return head_node


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        import collections
        q = collections.deque()
        head = root
        q.append(root)
        prev = TreeLinkNode(0)
        while q:
            len_q = len(q)
            for i in range(len_q):
                current_node = q.popleft()
                prev.next = current_node
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
                prev = current_node
            current_node.next = None
            prev = TreeLinkNode(0)

        return head

if __name__ == "__main__":
    head = generate_tree([1,2,3,4,5,6,7,8,9])
    s = Solution()
    head = s.connect(head)

    stack = []
    while head:
        stack.append(head)
        head = head.left
    for i in stack:
        while i:
            print i.val,
            i = i.next
        print