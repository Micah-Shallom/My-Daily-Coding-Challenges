"""
Creating a Stack using LinkedList

stack creation
isEmpty
push
pop
peek
delete
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Stack:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(node.value) for node in self.LinkedList]
        return " -> ".join(values)
    
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
        
    def push(self,value):
        new_node = Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head = new_node
        else:
            new_node.next = self.LinkedList.head
            self.LinkedList.head = new_node

    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            self.LinkedList.head = self.LinkedList.head.next

    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            headValue = self.LinkedList.head.value
            return headValue



stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
# print(stack.isEmpty())
print(stack)
print("-"*10)
stack.pop()
print(stack)
print("-"*10)
print(stack.peek())
        
        