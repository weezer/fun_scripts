# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        self.current = head

        self.small = ListNode(0)
        self.large = ListNode(0)
        self.smallhead = self.small
        self.largehead = self.large

        while self.current is not None:
            if self.current.val < x:
                self.small.next = self.current
                self.small = self.small.next
            else:
                self.large.next = self.current
                self.large = self.large.next
            self.current = self.current.next
        self.large.next = None
        self.small.next = self.largehead.next
        return self.smallhead.next




