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
    def traverseSLL (self):
        node = self.head
        while node :
            print(node.value)
            node = node.next

    def searchSLL(self,nodevalue):
        node=self.head
        while node:
            if nodevalue==node.value:
                print("value has been found")
                break
            node=node.next

    def deleteNode





sLL = SLinkedList()
sLL.insertSLL(1,0)
sLL.insertSLL(1,0)
sLL.insertSLL(5,1)
sLL.insertSLL(3,0)
sLL.insertSLL(10,2)
sLL.insertSLL(1,1)
sLL.traverseSLL()     
sLL.searchSLL(1)
for node in sLL:
    print(node.value)         