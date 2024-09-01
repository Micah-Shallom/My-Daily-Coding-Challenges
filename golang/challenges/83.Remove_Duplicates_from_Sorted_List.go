package challenges


// Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

// Example 1:

// Input: head = [1,1,2]
// Output: [1,2]
// Example 2:


// Input: head = [1,1,2,3,3]
// Output: [1,2,3]


func deleteDuplicates(head *ListNode) *ListNode { 
    if head == nil {
        return head
    }

	curr := head

	for curr != nil && curr.Next != nil {
		if curr.Val == curr.Next.Val {
			curr.Next = curr.Next.Next
		}else{
            curr = curr.Next
        }
	}


	return head
}