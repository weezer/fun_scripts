# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        stack1 = []
        stack2 = []
        current = head
        while current:
            if current.val < x:
                stack1.append(current.val)
            else:
                stack2.append(current.val)
        current = head
        while stack1:
            current.val = stack1.pop(0)
            current = current.next
        while stack2:
            current.val = stack2.pop(0)
            current = current.next
        return head