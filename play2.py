class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class CircularSLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCSLL(self,value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node

    def insertCSLL(self,value,location):
        new_node = Node(value)
        if self.head is None:
            return "The CSLL does not exist"
        else:
            if location == 0:
                new_node = Node(value)
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head
            elif location == 1:
                new_node.next = self.head
                self.tail.next = new_node
                self.tail = new_node
            else:
                index = 0
                node = self.head
                while index < location - 1:
                    node = node.next
                    index += 1
                new_node.next = node.next
                node.next = new_node

    def traverseCSLL(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
            if node == self.tail.next:
                break

    def searchCSLL(self,nodeValue):
        node = self.head
        while node:
            node = node.next
            if node.value == nodeValue:
                return f"The node value {node.value} exists"
            if node == self.tail.next:
                return "The node does not exist"
            
    def deleteNode(self,location):
        if self.head is None:
            return "The CSLL does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node == self.tail.next:
                            break   
                        node = node.next
                    node.next = self.head
                    self.tail = node



circularSLL = CircularSLinkedList()
circularSLL.createCSLL(1)
circularSLL.insertCSLL(1,1)
circularSLL.insertCSLL(2,0)
circularSLL.insertCSLL(7,0)
circularSLL.insertCSLL(70,2)
circularSLL.insertCSLL(5,0)
circularSLL.insertCSLL(4,0)
# circularSLL.traverseCSLL()
print(circularSLL.searchCSLL(70))
print([each.value for each in circularSLL])
circularSLL.deleteNode(1)
print([each.value for each in circularSLL])