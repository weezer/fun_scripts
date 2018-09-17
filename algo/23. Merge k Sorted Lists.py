import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self, nums):
        len_nums = len(nums)
        jump_num = (len_nums + 1) /2
        while True:
            for i in range(len_nums/2):
                self.merge_two_list(nums[i], nums[i + jump_num])
            if jump_num == 1:
                return nums[0]
            jump_num = (jump_num + 1) /2
            len_nums = (len_nums + 1) / 2

    def merge_two_list(self, first, second):
        if first is None and second is None:
            return None
        if first is None:
            return second
        if second is None:
            return first
        head = ListNode(0)
        current = head
        while first is not None and second is not None:
            if first.val < second.val:
                current.next = first
                first = first.next
            else:
                current.next = second
                second = second.next
            current = current.next
        if first is not None:
            current.next = first
        if second is not None:
            current.next = second
        return head.next

    def heap_sort_k(self, nums):
        h_list = []
        for i in nums:
            heapq.heappush(h_list, (i.val, i))
        head = ListNode(0)
        current = head
        while len(h_list) != 0:
            pos = heapq.heappop(h_list)
            current.next = pos
            if pos.next is not None:
                heapq.heappush(h_list, (pos.next.val, pos.next))
        return head.next





