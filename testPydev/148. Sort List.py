# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        slow_point, fast_point = head, head
        while fast_point.next and fast_point.next.next:
            slow_point = slow_point.next
            fast_point = fast_point.next.next
        right_point = slow_point.next
        slow_point.next = None
        left = self.sortList(head)
        right = self.sortList(right_point)

        current = (left, right)[right.val < left.val]
        head = current
        while left is not None and right is not None:
            if left.val > right.val:
                prev = right
                right = right.next
                current.next = prev
                current = current.next
            else:
                prev = left
                left = left.next
                current.next = prev
                current = current.next
        while left is not None or right is not None:
            if left is not None:
                prev = left
                left = left.next
                current.next = prev
                current = current.next
            else:
                prev = right
                right = right.next
                current.next = prev
                current = current.next

        return head



if __name__ == "__main__":
    head = ListNode(5)
    current = head
    for i in range(4,-1,-1):
        current.next = ListNode(i)
        current = current.next

    current = head
    # while current is not None:
    #     print current.val
    #     current = current.next
    s = Solution()
    head = s.sortList(head)
    while head is not None:
        print head.val
        head = head.next






