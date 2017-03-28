class Node(object):
    def __init__(self, val):
        self.name = id(self)
        self.val = val
        self.next = None


head = Node(0)
current = head
for i in range(1,4):
    current.next = Node(i)
    current = current.next
    if i == 3:
        current.next = Node(3)


