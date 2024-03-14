# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

ll1 = [1,2,4]
ll2 = [1,3,4,6,7,8]

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

head1 = Node(ll1[0])
head2 = Node(ll2[0])
x = head1
y = head2

for nodevalue in ll1[1:]:
    x.next = Node(nodevalue)
    x = x.next

for nodevalue in ll2[1:]:
    y.next = Node(nodevalue)
    y = y.next


def mergeTwoLists(list1: Node, list2:Node):
    #dummy node to store results
    dummyNode = Node(0)

    tail = dummyNode
    while True:

        #if any of the list gets completely empty, directly join all the elements of the other lists
        if list1 is None:
            tail.next =  list2
            break

        if list2 is None:
            tail.next = list1
            break

        if list1.value <= list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        
        tail = tail.next
    
    return dummyNode.next

    

def printLL(head):
    pointer = head

    while pointer:
        print(pointer.value)
        pointer = pointer.next

mergedHead = mergeTwoLists(head1,head2)
printLL(mergedHead)