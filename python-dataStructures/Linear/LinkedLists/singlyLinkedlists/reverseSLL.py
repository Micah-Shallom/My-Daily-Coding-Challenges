# recreating the whole single linkedlist concepts
# - instantiate the node and linkedlist(make iterable)
# - inserting a linkedlist functionality
# - traversing a linkedlist functionality by location
# - search a linkedlist by nodevalue
# - delete a node by location
# - delete all nodes


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self,value,location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == 1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                i = 0
                node = self.head
                while i < location - 1:
                    node = self.head.next
                    i += 1
                new_node.next = node.next
                node.next = new_node

    def traverseSLL(self,location):
        if self.head is None:
            return "The singly linkedlist does not exist"
        else:
            i  = 0
            node = self.head
            while i < location - 1:
                node = node.next
                i += 1
            return f"The node value {node.value} is here located at index location {location}"
        
    def searchSLL(self, nodeValue):
        if self.head is None:
            return "The singly linkedlist does not exist"
        else:
            node = self.head

            while node:
                if node.value == nodeValue:
                    break
                node = node.next
            return f"The nodeValue has been found. {node.value}"
        
    def deleteNode(self, location):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            if location == 0:
                self.head = self.head.next
            elif location == 1:
                i = 0
                node = self.head
                while node:
                    node = node.next
                    i += 1

                node.next = None
                self.tail = node
            else:
                i = 0
                node = self.head
                while i < location - 1 :
                    node = node.next
                    i += 1
                next_node = node.next
                node.next = next_node.next

    def reverseSLL(self):
        previous = None
        current = self.head
        next = None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

sLL = SLinkedList()
sLL.insertSLL(1,0)
sLL.insertSLL(2,0)
sLL.insertSLL(3,0)
sLL.insertSLL(8,1)
sLL.insertSLL(9,1)
sLL.insertSLL(8,2)
print([each.value for each in sLL])
# sLL.deleteNode(0)
sLL.deleteNode(4)
print(sLL.traverseSLL(3))
print(sLL.searchSLL(9))
print([each.value for each in sLL])

sLL.reverseSLL()
print("Reversed LinkedList ",[each.value for each in sLL])
