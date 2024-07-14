# recreating the whole single linkedlist concepts
# - instantiate the node and linkedlist(make iterable)
# - inserting a linkedlist functionality
# - traversing a linkedlist functionality by location
# - search a linkedlist by nodevalue
# - delete a node by location
# - delete all nodes


class Node:
    def __init__(self,value) -> None:
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
                index = 0
                node = self.head
                while index < location - 1:
                    node = node.next
                    index += 1
                new_node.next = node.next
                node.next = new_node

    def traverseSLL(self,location):
        if self.head is None:
            return "The Linked List does not exist"
        else:
            index = 0
            node = self.head
            while index < location - 1 :
                node = node.next
                index += 1
            print("The node {} exists".format(node.value))
    def searchSLL(self,nodeValue):
        if self.head is None:
            return "The LinkedList does not exist"
        else:
            node = self.head
            while node:
                if node.value == nodeValue:
                    print("The node value exists and has been seen")
                    break
                node = node.next
    def deleteNode(self, location):
        if self.head is None:
            return "The LinkedList does not exist"
        else:
            if location == 0:
                self.head = self.head.next
            elif location == 1:
                node = self.head
                while node is not None:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = None
                self.tail = node
            else:
                index = 0
                node = self.head
                while index < location - 1:
                    node = node.next
                    index += 1
                next_node =  node.next
                node.next = next_node.next

                
    

    

sLL = SLinkedList()
sLL.insertSLL(1,0)
sLL.insertSLL(1,0)
sLL.insertSLL(5,1)
sLL.insertSLL(3,0)
sLL.insertSLL(10,2)
sLL.insertSLL(1,1)
# sLL.traverseSLL(2)
# sLL.searchSLL(5)
# sLL.deleteNode(1)

print([each.value for each in sLL])
                
