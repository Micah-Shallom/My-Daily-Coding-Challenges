class Node:
    def __init__(self,value) -> None:
        self.prev = None
        self.value = value
        self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self,nodeValue):
        new_node = Node(nodeValue)
        new_node.next = None
        new_node.prev = None
        self.head = new_node
        self.tail = new_node

    def insertDLL(self, value , location):
        new_node = Node(value)
        if self.head is None:
            return "The double linkedlist does not exist"
        else:
            if location == 0:
                new_node.prev = None
                new_node.next = self.head
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
                if node is None:
                    return "Invalid Location"
                new_node.next = node.next
                new_node.prev = node
                new_node.next.prev = new_node
                node.next = new_node
                
    def traverseDLL(self):
        if self.head is None:
            return "The doubly linkedlist does not exist"
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next

    def reverseTraverseDLL(self):
        if self.head is None:
            return "The doubly linkedlist does not exist"
        node = self.tail
        while node:
            print(node.value)
            node = node.prev

    def searchDLL(self,value):
        node = self.head
        while node:
            if node.value == value:
                return f"Found = {node.value}"
            node = node.next
        return "Node exists not"
    
    def deleteNode(self, location):
        if self.head is None:
            return 'The DLL does not exist'
        else:
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
                while index < location -1 :
                    node = node.next
                    index += 1
                node.next = node.next.next
                node.next.prev = node

    def deleteAllNode(self):
        if self.head is None:
            return "The DLL does not exist"
        else:
            node = self.head
            while node:
                node.prev = None
                node = node.next
            self.head = None
            self.tail = None



doubleLL = DoublyLinkedList()
doubleLL.createDLL(5)
doubleLL.insertDLL(0,1)
doubleLL.insertDLL(0,0)
doubleLL.insertDLL(2,1)
doubleLL.insertDLL(6,2)
doubleLL.insertDLL(4,1)
doubleLL.insertDLL(3,1)
doubleLL.traverseDLL()
doubleLL.reverseTraverseDLL()
print(doubleLL.searchDLL(6))
print([node.value for node in doubleLL])
doubleLL.deleteNode(2)
print([node.value for node in doubleLL])
doubleLL.deleteAllNode()
print([node.value for node in doubleLL])



