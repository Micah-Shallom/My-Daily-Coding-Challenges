// You are given the head of a singly linked-list. The list can be represented as:
// L0 → L1 → … → Ln - 1 → Ln
// Reorder the list to be on the following form:
// L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
// You may not modify the values in the list's nodes. Only nodes themselves may be changed.

// Example 1:
// Input: head = [1,2,3,4]
// Output: [1,4,2,3]

// Example 2:
// Input: head = [1,2,3,4,5]
// Output: [1,5,2,4,3]

// Constraints:
// The number of nodes in the list is in the range [1, 5 * 104].
// 1 <= Node.val <= 1000

package challenges


func reorderSolution(head *Node){
	if head == nil || head.next == nil {
		return
	}
	
	// find the middle of the linkedlist
	middle := middleLLNode(head)

	//reverse the second half of the linkedlist
	reversedHead := reverseLL(middle.next)
	middle.next = nil

	c1 := head
	c2 := reversedHead

	var f1, f2 *Node

	for c1 != nil && c2 != nil {
		//backup
		f1 = c1.next
		f2 = c2.next

		// linking
		c1.next = c2
		c2.next = f1

		//move forward
		c1 = f1
		c2 = f2
	}

}


func middleLLNode(head *Node) *Node {
	slow := head
	fast := head

	for fast.next != nil && fast.next.next != nil {
		slow = slow.next
		fast = fast.next.next
	}
	return slow
}

func reverseLL(head *Node) *Node {
	prev := (*Node)(nil)
	curr := head
	next := (*Node)(nil)

	for curr != nil {
		next = curr.next
		curr.next = prev
		prev = curr
		curr = next
	}
	return prev
}

func ReorderList(){
	arr:= []int{1,2,3,4,5}
	head := createLL(arr)
	// head = reorderSolution(head)
	printLL(head)
}