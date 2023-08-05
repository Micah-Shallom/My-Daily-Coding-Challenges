class ListNode:
    def __init__(self,value=0) -> None:
        self.value = value
        self.next = None

arr = [1,2,3,4,5]

h = ListNode(arr[0])
v = h

for node in arr[1:]:
    v.next = ListNode(node)
    v = v.next


class Solution:
    def reverseLL(self,head):
        prev = None
        curr = head
        next = None

        while (curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
    def recurseReverseLL(self,head,prev=None,next=None):
        curr = head
        if curr == None:
            return prev
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        print(prev.value)
        return self.recurseReverseLL(curr, prev , next)

def printl(head):
    pointer = head
    while pointer:
        print(pointer.value , end=", ")
        pointer = pointer.next

inst = Solution()
printl(inst.recurseReverseLL(h))


