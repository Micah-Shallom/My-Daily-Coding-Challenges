// You are given two linked lists: list1 and list2 of sizes n and m respectively.

// Remove list1's nodes from the ath node to the bth node, and put list2 in their place.
// The blue edges and nodes in the following figure indicate the result:
// Build the result list and return its head.

// Example 1:
// Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
// Output: [10,1,13,1000000,1000001,1000002,5]
// Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

// Example 2:
// Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
// Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
// Explanation: The blue edges and nodes in the above figure indicate the result.

package challenges

func mergeSolution(list1, list2 *Node, a, b int) *Node {
	curr := list1
	i := 0

	for i < a-1 {
		curr = curr.next
		i++
	}
	head := curr

	for i <= b {
		curr = curr.next
		i++
	}

	head.next = list2
	
	for list2.next != nil {
		list2 = list2.next
	}
	list2.next = curr

	return list1
}

func MergeInBetween() {
	list1 := createLL([]int{10, 1, 13, 6, 9, 5})
	list2 := createLL([]int{1000000, 1000001, 1000002})
	head := mergeSolution(list1, list2, 3, 4)
	printLL(head)
}
