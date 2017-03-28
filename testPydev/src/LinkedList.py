class Node(object):
    def __init__(self, x):
        self.value = x
        self.next = []


firstNode = Node(0)
firstNode.next.append(firstNode)
firstNode.next.append(firstNode)
firstNode.next.append(firstNode)

