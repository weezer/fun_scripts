class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        new_node = head
        add_on = 0
        while l1 or l2 or add_on:
            result = 0
            if l1 is not None:
                result += l1.val
                l1 = l1.next
            if l2 is not None:
                result += l2.val
                l2 = l2.next
            new_node.next = ListNode((add_on + result) % 10)
            add_on = (add_on + result) / 10
            new_node = new_node.next
        return head.next

