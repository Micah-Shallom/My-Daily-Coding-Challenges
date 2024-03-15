// Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

// After doing so, return the head of the final linked list.  You may return any such answer.
// (Note that in the examples below, all sequences are serializations of ListNode objects.)

// Example 1:
// Input: head = [1,2,-3,3,1]
// Output: [3,1]
// Note: The answer [1,2,1] would also be accepted.

// Example 2:
// Input: head = [1,2,3,-3,4]
// Output: [1,2,4]

// Example 3:
// Input: head = [1,2,3,-3,-2]
// Output: [1]

package challenges

import "fmt"


func rzSolution(head *Node) *Node {
	dummy := &Node{value: 0, next: head}
	cumSum := 0
	nodeMap := make(map[int]*Node)

	curr := dummy

	for curr != nil{
		cumSum += curr.value
		nodeMap[cumSum] = curr
		curr = curr.next
	}

	cumSum = 0
	curr = dummy

	for curr != nil {
		cumSum += curr.value
		curr.next = nodeMap[cumSum].next
		curr = curr.next
	}
	fmt.Println(nodeMap)

	return dummy.next
}


func RemoveZeroSumSublists(){
	arr := []int{1,2,3,-3,-4}
	ll := createLL(arr)
	head := rzSolution(ll)
	printLL(head)
}