##The way i do it

arr = [1,4,6,7,4,3,5,6,7,6,5,4,3,3,54,6,7,9,8,6,5,4,6,4,3,5,5]


#setup the node class
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
            yield node #using a generative function to allow iterative function calls
            node = node.next

    def insertNode(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

sLL = LinkedList()
for idx in range(len(arr)):
    sLL.insertNode(arr[idx])

print()

print([node.value for node in sLL])
            







