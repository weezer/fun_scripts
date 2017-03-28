class Node(object):
    def __init__(self):
        self.value = None
        self.children = {}
        self.num = 0


class Trie(object):
    def __init__(self):
        self.root = Node()

    def add_word(self, word):
        current = self.root
        for i in word:
            if not current.children.get(i):
                current.children[i] = Node()
                current.children[i].value = i
            current = current.children.get(i)
        current.num += 1

    def search_word(self, word):
        current = self.root
        for i in word:
            if not current.children.get(i):
                return False
            current = current.children.get(i)
        return True

    def get_num_list(self):
        current = self.root
        num_map = {}
        self.get_num(self.root, num_map, "")
        return num_map

    def get_num(self, node, num_map, word):
        word = word + (node.value, "")[node.value == None]
        if node.num > 0:
            num_map[word] = node.num
        for i in node.children.values():
            self.get_num(i, num_map, word)





if __name__ == "__main__":
    trie = Trie()
    with open("100west.txt") as file:
        word_list = [x for x in file.read().split()]
    for i in word_list:
        trie.add_word(i)
    word_list = trie.get_num_list()
    sorted_word_list = sorted(word_list.items(), key=lambda(k, v): v, reverse=True)
    print sorted_word_list[0:10]