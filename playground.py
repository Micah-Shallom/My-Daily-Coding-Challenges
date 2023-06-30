# recreating the whole single linkedlist concepts
# - instantiate the node and linkedlist(make iterable)
# - inserting a linkedlist functionality
# - traversing a linkedlist functionality
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
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                node = self.head
                index = 0
                while index < location - 1:
                    node = node.next
                    index += 1
                newNode.next = node.next
                node.next = newNode
    def traverseSLL(self,location):
        if self.head is None:
            print("The singly linkedlist does not exist")
        else:
            node = self.head
            index = 0
            while index < location -1 :
                node = node.next
                index += 1
            print(node.value)
    def searchSLL(self,nodeValue):
        if self.head is None:
            print("The singly linkedlist does not exist")
        else:
            node = self.head
            index = 0
            while node:
                if node.value == nodeValue:
                    break
                node = node.next
                index += 1
            print(f"The node {node.value} exists")
    def deleteNode(self, location):
        if self.head is None:
            print("The singly linkedlist does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    index = 0
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                        index += 1
                    node.next = None
                    self.tail = node
            else:
                node = self.head
                index = 0
                while index < location - 1 :
                    node = node.next
                    index += 1
                newNode = node.next
                node.next = newNode.next

                

                



                


singlylinkedlist = SLinkedList()
# index = [randint(0,1) for _ in range(10)]
# value = [randint(1,30) for _ in range(10)]
# [singlylinkedlist.insertSLL(each[0],each[1]) for each in zip(value,index)]

singlylinkedlist.insertSLL(3,0)
singlylinkedlist.insertSLL(4,0)
singlylinkedlist.insertSLL(34,1)
singlylinkedlist.insertSLL(34,1)
singlylinkedlist.insertSLL(45,1)
singlylinkedlist.insertSLL(45,3)
singlylinkedlist.traverseSLL(3)
singlylinkedlist.searchSLL(34)
singlylinkedlist.deleteNode(2)
singlylinkedlist.deleteNode(0)
singlylinkedlist.deleteNode(1)
print([each.value for each in singlylinkedlist])
    
