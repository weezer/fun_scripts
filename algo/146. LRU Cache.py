class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.kv = {}
        self.head = None
        self.capacity = capacity
        self.number = 0
        self.lastP = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.kv.get(key):
            current = self.kv.get(key)
            if self.head == current:
                return self.head.value
            if self.lastP == current:
                self.lastP = current.prev
                self.lastP.next = None
                current.next = self.head
                self.head.prev = current
                self.head = current
                current.prev = self.head
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
                current.next = self.head
                self.head.prev = current
                self.head = current
                current.prev = current
            return current.value
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.kv.get(key):
            current = self.kv.get(key)
            current.value = value
            if self.head != current:
                if self.lastP == current:
                    self.lastP = current.prev
                    self.lastP.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                current.next = self.head
                self.head.prev = current
                self.head = current
                current.prev = self.head
        else:
            new_node = LinkedList()
            self.kv[key] = new_node
            new_node.key = key
            new_node.value = value
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            new_node.prev = new_node
            self.head = new_node
            if self.capacity == self.number:
                self.kv.pop(self.lastP.key)
                self.lastP = self.lastP.prev
                self.lastP.next = None
            else:
                self.number += 1
                if self.lastP is None:
                    self.lastP = new_node
        print self.kv


        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)


class LinkedList(object):
    def __init__(self):
        self.key = None
        self.value = None
        self.prev = None
        self.next = None

if __name__ == "__main__":
    lruc = LRUCache(10)
    lruc.put(10,13)
    lruc.put(3,17)
    lruc.put(6,11)
    lruc.put(10,5)
    lruc.put(9,10)
    print lruc.get(13)
    lruc.put(2,19)
    print lruc.get(2)
    print lruc.get(3)
    lruc.put(5,25)
    print lruc.get(8)
    lruc.put(9, 22)
    print lruc.get(3)
    print lruc.get(4)
# ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
# [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
# [null,null,null,null,null,null,-1,null,19,17,null,-1,null,null,null,-1,null,-1,5,-1,12,null,null,3,5,5,null,null,1,null,-1,null,30,5,30,null,null,null,-1,null,-1,24,null,null,18,null,null,null,null,-1,null,null,18,null,null,-1,null,null,null,null,null,18,null,null,24,null,4,29,30,null,12,-1,null,null,null,null,29,null,null,null,null,17,-1,18,null,null,null,-1,null,null,null,20,null,null,null,-1,18,18,null,null,null,null,20,null,null,null,null,null,null,null]
# [null,null,null,null,null,null,-1,null,19,17,null,-1,null,null,null,-1,null,-1,5,-1,12,null,null,3,5,5,null,null,1,null,-1,null,30,5,30,null,null,null,-1,null,-1,24,null,null,18,null,null,null,null,-1,null,null,18,null,null,-1,null,null,null,null,null,18,null,null,-1,null,4,29,30,null,12,-1,null,null,null,null,29,null,null,null,null,17,22,18,null,null,null,-1,null,null,null,20,null,null,null,-1,18,18,null,null,null,null,20,null,null,null,null,null,null,null]