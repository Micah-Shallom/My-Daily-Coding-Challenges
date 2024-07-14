class Queue:
    def __init__(self, maxSize) -> None:
        self.items = [None] * maxSize
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self) -> str:
        return " ".join([str(x) for x in self.items])
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top+1 == self.maxSize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.top == -1:
            return True
        else: return False

    def enqueue(self,value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1 :
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of the queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "There is no element in the Queue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

    def peek(self):
        if self.isEmpty():
            return "There is no element in the Queue"
        else:
            return self.items[self.start]
        
    def delete(self):
        self.items = [None] * self.maxSize
        self.top = -1
        self.start =  -1
        
customQueue = Queue(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(5) 
print(customQueue.dequeue())
# customQueue.delete()
print(customQueue)