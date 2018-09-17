class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def createBST(keys):
    counter_num = 0
    if len(keys) > 0:
        head = Node(keys[0])
        keys = keys[1:]
        print counter_num
    for i in keys:
        counter_num = insert(head, i, counter_num)
        print counter_num


def insert(root, key, counter):
    if root is None:
        root = Node(key)
        return counter
    else:
        if root.val > key:
            if root.left is None:
                root.left = Node(key)
                return counter + 1
            else:
                return insert(root.left, key, counter + 1)
        else:
            if root.right is None:
                root.right = Node(key)
                return counter + 1
            else:
                return insert(root.right, key, counter + 1)

if __name__ == "__main__":
    createBST([1,2,3])