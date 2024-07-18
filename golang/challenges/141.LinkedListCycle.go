// Given head, the head of a linked list, determine if the linked list has a cycle in it.

// There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

// Return true if there is a cycle in the linked list. Otherwise, return false.

// Example 1:

// Input: head = [3,2,0,-4], pos = 1
// Output: true
// Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
// Example 2:

// Input: head = [1,2], pos = 0
// Output: true
// Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
// Example 3:

// Input: head = [1], pos = -1
// Output: false
// Explanation: There is no cycle in the linked list.

package challenges

import "fmt"

func hcSolution(arr []int) (res bool){
	new_head := createLL(arr)
	hashmap := map[*Node]int{}

	pointer := new_head
	for pointer != nil{
		hashmap[pointer] = pointer.value
		pointer = pointer.next

		if _, found := hashmap[pointer]; found{
			return true
		}
	}
	fmt.Println(hashmap)
	return false
}

func thSolution(arr []int) (res bool){
	head := createLL(arr)

	if head == nil {
		return false
	}

	tort := head
	hare := head.next

	for tort != nil && hare != nil {
		if tort == hare {
			return true
		}
		tort = tort.next
		if hare.next == nil {
			return false
		}else{
			hare = hare.next.next
		}
	}
	return false
}

func HasCycle(){
	head := []int{3,2,0,-4}
	fmt.Println(hcSolution(head))
}