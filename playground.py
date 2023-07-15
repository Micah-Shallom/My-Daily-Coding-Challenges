class Node:
    def __init__(self,value):
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
            if node == self.tail.next:
                break
            node = node.next
    
    def createCSLL(self,value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        return "The circular singly linkedlist has been created"

    def insertCSLL(self,value,location):
        new_node = Node(value)
        if self.head is None:
            return "The circular linkedlist does not exist"
        else:
            if location == 0 :
                new_node = Node(value)
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
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
                nextNode = node.next
                node.next = new_node
                new_node.next = nextNode
                return "Items have been successfully inserted"

    

circularSLL = CircularSLinkedList()
circularSLL.createCSLL(1)
circularSLL.insertCSLL(8,0)
circularSLL.insertCSLL(2,1)
circularSLL.insertCSLL(7,1)
circularSLL.insertCSLL(4,1)
circularSLL.insertCSLL(3,0)
circularSLL.insertCSLL(10,3)
circularSLL.insertCSLL(4,0)

print([each.value for each in circularSLL])

