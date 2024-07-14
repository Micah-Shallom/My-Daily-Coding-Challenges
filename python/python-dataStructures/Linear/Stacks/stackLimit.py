"""
Creating a Stack using Lists with fixed size

stack creation
isEmpty
isFull
push
pop
peek
delete
"""

class Stack:
    def __init__(self,maxsize) -> None:
        self.maxsize = maxsize
        self.list = [] 

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(val) for val in self.list]
        print('\n'.join(values))

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxsize:
            return True
        else:
            return False
        
    def push(self,value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "New value has been added to the stack"
        
    def pop(self):
        if self.isEmpty():
            return "The stack is empty, Nothing to pop"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return "The stack is empty, Nothing to peek"
        else:
            return self.list[-1]
    
    def deleteAll(self):
        self.list = None


stack = Stack(5)
print(stack.isEmpty())
print(stack.isFull())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.peek())
print(stack)
print(stack.deleteAll())
