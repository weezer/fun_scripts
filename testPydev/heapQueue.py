class HeapQueue(object):
    def __init__(self, in_lst = []):
        self.num_count = 0
        self.heap_lst = []

    def add_node(self, num):
        self.num_count += 1
        self.heap_lst.append(num)
        self.per_up()

    def per_up(self):
        len_lst = len(self.heap_lst)
        pos = len_lst
        while self.heap_lst[pos-1] < self.heap_lst[pos/2-1] and pos > 1:
            temp = self.heap_lst[pos-1]
            self.heap_lst[pos-1] = self.heap_lst[pos/2-1]
            self.heap_lst[pos/2-1] = temp
            pos /= 2

    def heap_pop(self):
        top = self.heap_lst[0]
        self.heap_lst[0] = self.heap_lst[self.num_count - 1]
        self.num_count -= 1
        self.per_down()
        self.heap_lst.pop()
        return top

    def per_down(self):
        pos = 0
        while (pos + 1) * 2 <= self.num_count:
            if (pos + 1) * 2 > self.num_count:
                min_child = self.num_count - 1
            else:
                min_child = [(pos + 1) * 2, (pos + 1) * 2 - 1][self.heap_lst[(pos + 1) * 2 - 1] < self.heap_lst[(pos +
                                                                                                               1) * 2]]
            print self.heap_lst[min_child]
            if self.heap_lst[pos] > self.heap_lst[min_child]:
                temp = self.heap_lst[pos]
                self.heap_lst[pos] = self.heap_lst[min_child]
                self.heap_lst[min_child] = temp
                pos = min_child
            else:
                break

    def __str__(self):
        return self.heap_lst[:self.num_count]


if __name__ == "__main__":
    hq = HeapQueue()
    for i in range(8, 0, -1):
        hq.add_node(i)
    print hq.heap_lst
    print hq.heap_pop()
    print hq.heap_lst