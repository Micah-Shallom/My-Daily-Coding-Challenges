#New method learnt

arr = [1,2,3,4,5]

class ListNode:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None


l = ListNode(arr[0]) #keeping track of our head
v = l

for idx,nodeValue in enumerate(arr[1:]):
    v.next = ListNode(nodeValue)
    v = v.next


def printLL(head):
    pointer = head

    while pointer:
        print(pointer.value, end=', ')
        pointer = pointer.next

class Solution:
    def reverseLL(self, head):
        prev = None
        curr = head
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next 

        return prev
        
    # def recursiveReversal(self,head):

    #     def recurse(prev,curr):
    #         if curr is None:
    #             return prev
        
    #     next = head.next
    #     head.next = prev
    #     return recurse(prev=curr,curr=next)

    
inst = Solution()
rev = inst.recursiveReversal(l)
printLL(rev)