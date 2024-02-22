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

for nodeValue in ll1[1:]:
    x.next = Node(nodeValue)
    x = x.next
for nodeValue in ll2[1:]:
    y.next = Node(nodeValue)
    y = y.next

def printLL(head):
    pointer = head

    while pointer:
        print(pointer.value, end=" ")
        pointer = pointer.next


def mergeLL(head1: Node, head2:Node) -> Node:
    dummyNode = Node(0)

    tail = dummyNode

    while True:
        if head1 is None:
            tail.next = head2
            break
        if head2 is None:
            tail.next = head1
            break

        if head1.value <= head2.value:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        
        tail = tail.next

    return dummyNode.next


mergedHead = mergeLL(head1, head2)
printLL(mergedHead)
