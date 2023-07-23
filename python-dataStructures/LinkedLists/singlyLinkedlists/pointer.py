#New method learnt

arr = [1,4,6,7,4,3,5,6,7,6,5,4,3,3,54,6,7,9,8,6,5,4,6,4,3,5,5]

class ListNode:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None


l = ListNode(arr[0]) #keeping track of our head
v = l

for idx,nodeValue in enumerate(arr[1:]):
    v.next = ListNode(nodeValue)
    v = v.next

pointer = l

while pointer:
    print(pointer.value, end=', ')
    pointer = pointer.next


    