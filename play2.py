class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
        
class Stack:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()

    def __str__(self) -> str:
        values = [str(node.value) for node in self.LinkedList]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else: return False

    def push(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.LinkedList.head = new_node
        else:
            new_node.next = self.LinkedList.head
            self.LinkedList.head = new_node

    def pop(self):
        if self.isEmpty():
            return "There is nothing to pop out"
        else:
            self.LinkedList.head = self.LinkedList.head.next
    
    def peek(self):
        if self.isEmpty():
            return "The Stack is empty"
        else:
            return self.LinkedList.head.value
        

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack)
print(stack.peek())
