class Queue:
    def __init__(self) -> None:
        self.items = []

    def __str__(self) -> str:
        return " ".join([str(each) for each in self.items])
    
    def isEmpty(self):
        if self.items == []:
            return True
        else: return False

    def enqueue(self,value):
        self.items.append(value)
        return "A value has been added to the queue"
    
    def dequeue(self):
        if self.isEmpty():
            return 'The queue is empty'
        else:
            self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.items[0]
        
    def delete(self):
        self.items = None
        return self.items
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)
queue.dequeue()
print(queue)