'''
Created on Apr 7, 2014

@author: Weezer
'''

class Node:
    def __init__(self, initiaData):
        self.data = initiaData
        self.next = None
    def setData(self, data):
        self.data = data
    def setNext(self, newNode):
        self.next = newNode
        
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    
class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head) 
        self.head = temp
        print self.head.getData()
    def size(self):
        current = self.head
        count = 0
        while current != None:
#             print current.getNext().getData()
            current = current.getNext()
            count += 1
        return count
    def search(self, item):
        current = self.head
        found = False
        while not found and current.getNext() != None:
            if current.getData() != item:
                current = current.getNext()
            else:
                found = True
        return found
    def remove(self, item):
        previous = current = self.head
        while current.getNext() != None:
            if current.getData() != item:
                previous = current
                current = current.getNext()
            else:
                previous.setNext(current.getNext())
                return "Deleted!"
        return "Not Found"
        