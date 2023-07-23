class Node:
    def __init__(self, value) -> None:
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
            if node.next == self.tail.next:
                break
            node = node.next

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
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:
                new_node.next = self.tail.next
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

    def searchSLL(self,value):
        if self.head is None:
            return "The CSLL does not exist"
        else:
            node = self.head
            while node:
                if node.value == value:
                    return f"The node value has been found {node.value} "
                node = node.next
            return "The node value is missing"
    
    def traverseCSLL(self):
        if self.head is None:
            return "The CSLL does not exist"
        else:
            node = self.head
            while node:
                print(node.value)
                if node.next == self.tail.next:
                    break
                node = node.next

    def deleteNode(self,location):
        if self.head is None:
            return "The CSLL does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head

circularSLL = CircularSLinkedList()
circularSLL.createCSLL(5)
circularSLL.insertCSLL(1,0)
circularSLL.insertCSLL(1,0)
circularSLL.insertCSLL(3,1)
circularSLL.insertCSLL(7,2)
circularSLL.insertCSLL(45,0)
circularSLL.insertCSLL(32,1)
circularSLL.insertCSLL(70,2)
print(circularSLL.searchSLL(7))
circularSLL.traverseCSLL()
print([node.value for node in circularSLL])
circularSLL.deleteNode(0)
print([node.value for node in circularSLL])