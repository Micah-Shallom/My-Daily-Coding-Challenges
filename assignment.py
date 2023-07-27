# Assignment 1
# ▪ Write a Python code that implements the basic operations of an
# array? (Must include the Update operation)

# ▪ Implement an enqueue and dequeue operation in Python?'




# ▪ Write a Python code that implements the basic operations of a
# linked list?
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

    def createCSLL(self,value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node


    def insertNode(self,value):
        new_node = Node(value)
        if self.head is None:
            re



