'''
Created on May 9, 2014

@author: Weezer
'''
import string 
from operator import itemgetter
class Node:
    def __init__(self):
        self.value = None
        self.children = {}  #child is of type {char, Node}
        self.num = 0
        
class Tire:
    def __init__(self):
        self.root = Node()
    
    def insert(self, key): # key is string, lower case string.
        node = self.root
        for chr in key:
            if chr not in node.children:
                child = Node()
                node.children[chr] = child
                node = child
            else:
                node = node.children[chr]
        node.value = key
        node.num += 1
    
    def search(self, key):
        node = self.root
        for chr in key:
            if chr in node.children:
                node = node.children[chr]
            else:
                return None
        return node.value
    
    def display_node(self, node):
        if(node.value != None):
            print "%s : %d" % (node.value, node.num)
#             return [node.valu, node.num]
        for chr in string.lowercase:
            if chr in node.children:
                self.display_node(node.children[chr])
        
    def display(self):
        self.display_node(self.root)
        
    def getTopTen(self):
        nodeLst = []
        self.getNodeValue(self.root, nodeLst)
        return nodeLst
        
    def getNodeValue(self, node, nodeLst = []):
        if node.value != None:
            nodeLst.append([node.value, node.num])
        for chr in string.ascii_lowercase:
            if chr in node.children:
                self.getNodeValue(node.children[chr], nodeLst)
            
if __name__ == '__main__':
#     pass
    with open('../../100west.txt', 'rb') as file:
        text = file.read()
#         print text
        inputText = [word.strip(string.punctuation) for word in text.split()]
    print inputText
    trie = Tire()
    for word in inputText:
#         print word
        trie.insert(word)
#     trie.display()
    print trie.search('THaE')
    lst = trie.getTopTen()
    lst.sort(key = lambda k : k[1])
    print lst[:len(lst)-11:-1]
    
    print '================= END ====================='