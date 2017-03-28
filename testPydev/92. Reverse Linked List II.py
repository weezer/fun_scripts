# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        import collections
        q = collections.deque()
        prev = ListNode(0)
        prev.next = head
        current = head
        head = prev
        start_pos, end_pos = 0, 0
        while end_pos < n:
            start_pos += 1
            end_pos += 1
            if start_pos < m:
                prev = prev.next
                current = current.next
                continue
            q.append(current)
            current = current.next
        # print len(q)
        end_next = current

        while q:
            current = q.pop()
            prev.next = current
            prev = prev.next
        prev.next = end_next
        return head.next


if __name__ == "__main__":
    head = ListNode(1)
    current = head
    for i in range(2, 3):
        prev = current
        current = ListNode(i)
        prev.next = current

    s = Solution()
    r_head = s.reverseBetween(head, 1, 2)
    while r_head is not None:
        print r_head.val
        r_head = r_head.next
