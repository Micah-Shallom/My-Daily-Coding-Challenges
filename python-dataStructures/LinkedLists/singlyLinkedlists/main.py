class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class SLinkendList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0: #insert in the beginning
                newNode.next = self.head
                self.head = newNode
            elif location == 1: #insert in the end
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
    #traversing through a singly linkend list
    def traverseSLL(self):
        if self.head is None:
            print("The singly linkend list does not exist")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
    #searching for a given value in a linkendlist
    def searchSLL(self, nodeValue):
        if self.head is None:
            return "The singly linkend list does not exist"
        else:
            node = self.head
            while node:
                if node.value == nodeValue:
                    return f"The value {node.value} exists"
                node = node.next
            return "The node value does not exist in the LinkendList"
    #deleting nodes from a LinkedList
    def deleteNode(self, location):
        if self.head is None:
            print("The LinkedList does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head == self.head.next
            if location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail =  node
            else:
                tempNode = self.head
                index = 0

                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    

            

singlyLinkendList = SLinkendList()
singlyLinkendList.insertSLL(1,1)
singlyLinkendList.insertSLL(2,1)
singlyLinkendList.insertSLL(12,1)
singlyLinkendList.insertSLL(3,2)
singlyLinkendList.insertSLL(5,1)
print([node.value for node in singlyLinkendList])
singlyLinkendList.traverseSLL()
print(singlyLinkendList.searchSLL(3))


# NORMAL INSTANTIATION OF A SINGLE LINKEDLIST CONTAINING HEAD, TAIL AND 2 NODES
# singlyLinkedLists = SLinkedLists()
# node1 = Node(1)
# node2 = Node(2)

# singlyLinkedLists.head = node1
# singlyLinkedLists.tail = node2
# singlyLinkedLists.head.next = node2


# INSERTION ALGORITHMS IN A LINKEDLIST--------------------------------------------------------------


