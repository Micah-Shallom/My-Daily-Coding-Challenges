#Implementing a stack with a list


class Stack:
    def __init__(self) -> None:
        self.list = []

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    #isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    
    #push
    def push(self,value):
        self.list.append(value)
        return "The element has been inserted successsfully"
    
    #pop
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            self.list.pop()
    #peek

    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list)-1]
            
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
    