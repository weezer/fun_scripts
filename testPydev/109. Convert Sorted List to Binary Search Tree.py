# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def dfs_generate_balanced_tree(node):
            if not node.next:
                return TreeNode(node.val)
            head = node
            slow = node
            fast = node
            prev = node
            while fast.next and fast.next.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next
            if prev.next and prev == slow:
                slow = prev.next
            prev.next = None
            tree_node = TreeNode(slow.val)
            tree_node.left = dfs_generate_balanced_tree(head)
            if slow.next:
                tree_node.right = dfs_generate_balanced_tree(slow.next)
            return tree_node

        return dfs_generate_balanced_tree(head)


def pre_order(head):
    if head.left:
        pre_order(head.left)
    print head.val
    if head.right:
        pre_order(head.right)


if __name__ == "__main__":
    head = ListNode(0)
    current = head
    # for i in range(1, 10):
    #     current.next = ListNode(i)
    #     current = current.next
    s = Solution()
    tree_head = s.sortedListToBST(head)
    # print tree_head.val
    pre_order(tree_head)