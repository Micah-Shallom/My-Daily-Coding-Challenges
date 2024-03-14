class Node:
    def __init__(self,value) -> None:
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


class Queue:
    def __init__(self) -> None:
        self.LinkedList = LinkedList()

    def __str__(self) -> str:
        values = [str(node.value) for node in self.LinkedList]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else: return False

    def enqueue(self,value):
        new_node = Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head = new_node
            self.LinkedList.tail = new_node
        else:
            self.LinkedList.tail.next = new_node
            self.LinkedList.tail =  new_node
        
    def dequeue(self):
        if self.isEmpty():
            print("The Queue is empty")
        else:
            node = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else: 
                self.LinkedList.head = self.LinkedList.head.next
            return node
        
    def peek(self):
        if self.isEmpty():
            print("The Queue is empty")
        else:
            return self.LinkedList.head

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue)
queue.dequeue()
print(queue)
    