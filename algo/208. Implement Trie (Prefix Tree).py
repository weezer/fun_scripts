class Node(object):
    def __init__(self):
        self.num = 0
        self.hash_map = {}


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for i in word:
            if current.hash_map.get(i) is None:
                current.hash_map[i] = Node()
            current = current.hash_map.get(i)
        current.num += 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for i in word:
            if current.hash_map.get(i) is None:
                return False
            current = current.hash_map.get(i)
        if current.num != 0:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for i in prefix:
            if current.hash_map.get(i) is None:
                return False
            current = current.hash_map.get(i)
        return True


        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    s = Trie()
    s.insert("aa")
    s.insert("bb")
    s.insert("ab")
    s.insert("aa")
    print s.root.hash_map['a'].hash_map['a'].num
    print s.search("aa")
    print s.startsWith("a")