# class Node(object):
#     def __init__(self, val):
#         self._val = val
#         self.next = None
#
#
# def find_nth_to_last(_node, k):
#     if not _node:
#         return 0
#     count = find_nth_to_last(_node.next, k)
#     if count == k:
#         print _node._val
#     count += 1
#     return count
#
#
# if __name__ == "__main__":
#
#     head = Node(1)
#     current = head
#     for i in range(2, 5):
#         current.next = Node(i)
#         current = current.next
#
#     find_nth_to_last(head, 1)


def recursion(num):
    if num > 3:
        return
    print num
    recursion(num+1)
    print num

recursion(1)