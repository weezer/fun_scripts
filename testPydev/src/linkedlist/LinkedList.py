'''
Created on Apr 7, 2014

@author: Weezer
'''

class Node():
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
    
class LinkedList():
    def __init__(self, head):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self, newNode):
        