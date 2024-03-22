// Given the head of a singly linked list, return true if it is a
// palindrome
//  or false otherwise.

// Example 1:
// Input: head = [1,2,2,1]
// Output: true

// Example 2:
// Input: head = [1,2]
// Output: false

package challenges

import "fmt"

func palindromeSolution(head *Node) bool {
	arr := []int{}
	curr := head

	for curr != nil {
		arr = append(arr, curr.value)
		curr = curr.next
	}

	rP := len(arr) - 1

	for lp := 0 ; lp <= rP; lp++ {
		if arr[lp] != arr[rP]{
			return false
		}else{
			rP--
		}
	}
	return true
}

func PalindromeLL(){
	arr := []int{1,2,2,1}
	head := createLL(arr)
	fmt.Println(palindromeSolution(head))
}