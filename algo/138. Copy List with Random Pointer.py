# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head
        import Queue
        q = Queue.deque()
        q.append(head)
        kv = {}
        prev = RandomListNode(0)
        dummy_head = prev
        while q:
            current = q.popleft()
            prev.next = kv.get(current.label, RandomListNode(current.label))
            kv[current.label] = prev.next
            if current.next:
                q.append(current.next)
            if current.random:
                kv[current.random.label] =  kv.get(current.random.label, RandomListNode(current.random.label))
                prev.next.random = kv[current.random.label]
            prev = prev.next
        return dummy_head.next

if __name__ == "__main__":
    s = Solution()
    nums = [0] + [RandomListNode(i) for i in range(1, 6)]
    nums[1].next = nums[2]
    nums[1].random = nums[3]
    nums[2].next = nums[3]
    nums[2].random = nums[4]
    nums[3].next = nums[4]
    nums[3].random = nums[1]
    nums[4].next = nums[5]
    for i in nums[1:]:
        print i.label
        print i
        print i.next
        print i.random
    print
    print
    s.copyRandomList(nums[1])
    for i in nums[1:]:
        print i.label
        print i
        print i.next
        print i.random
