# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


#[1,2,3,3,4,4,5] -> [1,2,5]
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pseudohead = ListNode(None)
        pseudohead.next = head

        if head is None:
            return head
        else:
            pseudohead.val = head.val
        current = pseudohead
        while current.next is not None:
            nextval = current.next
            if nextval.next is not None and nextval.val == nextval.next.val:
                nextval.next = nextval.next.next
                while nextval.next is not None and nextval.val = nextval.next.val:
                    nextval.next = nextval.next.next
                current = current.next
            else:
                current = current.next
        return pseudohead.next