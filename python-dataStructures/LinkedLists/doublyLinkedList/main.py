#creating Double Linkedlist

"""
- create double linkedlist
- insert node
- search
- traverse
- reverseTraverse
- delete node
- delete all nodes
"""


class Node:
    def __init__(self,value) -> None:
        self.prev = None
        self.value = value
        self.next = None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self,value):
        new_node = Node(value)
        new_node.next = None
        new_node.prev = None
        self.head = new_node
        self.tail = new_node

    def insertDLL(self,value,location):
        new_node = Node(value)
        if self.head is None:
            return "The DLL does not exist"
        else:
            if location == 0:
                new_node.next = self.head
                new_node.prev = None
                self.head.prev = new_node
                self.head = new_node
            elif location == 1:
                new_node.next = None
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                index = 0
                node = self.head
                while index < location - 1:
                    node = node.next
                    index += 1
                new_node.next = node.next
                new_node.prev = node
                node.next.prev = new_node
                node.next = new_node

    def traverseDLL(self):
        if self.head is None:
            return "The DLL does not exist"
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
    def reverseTraverseDLL(self):
        print("-"*20)
        if self.head is None:
            return "The DLL does not exist"
        else:
            node = self.tail
            while node:
                print(node.value)
                node = node.prev

    def searchDLL(self,value):
        if self.head is None:
            return "The DLL does not exist"
        else:
            node = self.head
            while node:
                if node.value == value:
                    return f"THe value has been found {node.value}"
                node = node.next
            return "The value does not exist"
    
    def deleteNode(self,location):
        if self.head is None:
            return f"The DLL does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.next.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail.prev.next = None
                    self.tail = self.tail.prev
            else:
                index = 0
                node = self.head
                while index < location - 1:
                    node = node.next
                    index += 1
                node.next = node.next.next
                node.next.prev = node

    def deleteAll(self):
        if self.head is None:
            return "The DLL does not exist"
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node:
                    node.prev = None
                    node = node.next
                self.head = None
                self.tail = None

doubleLL = DoubleLinkedList()
doubleLL.createDLL(5)
doubleLL.insertDLL(4,0)
doubleLL.insertDLL(2,1)
doubleLL.insertDLL(5,1)
doubleLL.insertDLL(9,1)
doubleLL.insertDLL(7,3)
doubleLL.traverseDLL()
doubleLL.reverseTraverseDLL()
print(doubleLL.searchDLL(9))
print([node.value for node in doubleLL])
# doubleLL.deleteNode(0)
# print([node.value for node in doubleLL])
doubleLL.deleteNode(2)
print([node.value for node in doubleLL])
doubleLL.deleteAll()
print([node.value for node in doubleLL])