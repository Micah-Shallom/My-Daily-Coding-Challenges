

class Node:
    def __init__(self,value) -> None:
        self.prev = None
        self.value = value
        self.next = None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def check_node(self):
        if self.head is None:
            print("The DLL is empty")

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
        self.check_node()
        if location == 0:
            new_node.next = self.head
            new_node.prev =  None
            new_node.next.prev = new_node
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
            node.next = new_node
            new_node.next.prev = new_node

    def searchDLL(self,value):
        self.check_node()
        node = self.head
        while node:
            if node.value == value:
                return f"The node value {node.value} has been found"
            node = node.next
        return "The node value does not exist"
    
    def traverseDLL(self):
        self.check_node()
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def reverseTraverseDLL(self):
        print("---------")
        self.check_node()
        node = self.tail
        while node:
            print(node.value)
            node = node.prev

    def deleteNode(self,location):
        self.check_node()
        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif location == 1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        else:
            index = 0
            node = self.head
            while index < location - 1:
                node = node.next
                index += 1
            node.next = node.next.next
            node.next.prev = node




doubleLL = DoubleLinkedList()
doubleLL.createDLL(5)
doubleLL.insertDLL(2,0)
doubleLL.insertDLL(3,1)
doubleLL.insertDLL(3,1)
doubleLL.insertDLL(4,2)
doubleLL.insertDLL(7,2)
# print(doubleLL.searchDLL(7))
# doubleLL.traverseDLL()
# doubleLL.reverseTraverseDLL()
print([node.value for node in doubleLL])
doubleLL.deleteNode(0)
print([node.value for node in doubleLL])
doubleLL.deleteNode(1)
print([node.value for node in doubleLL])
doubleLL.deleteNode(2)
print([node.value for node in doubleLL])