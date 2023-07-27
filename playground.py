#circular singly linkedlist


class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class CircularSLinkedList:
    def __init__(self):
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

    def insertNode(self,value,location):
        new_node =  Node(value)
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
        
    
circularSLL = CircularSLinkedList()
circularSLL.createCSLL(2)
circularSLL.insertNode(1,0)
circularSLL.insertNode(1,0)
circularSLL.insertNode(2,1)
circularSLL.insertNode(4,1)
circularSLL.insertNode(7,0)
circularSLL.insertNode(7,0)
circularSLL.insertNode(5,2)

print([node.value for node in circularSLL])

