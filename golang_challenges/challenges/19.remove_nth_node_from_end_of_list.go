// Given the head of a linked list, remove the nth node from the end of the list and return its head.
package challenges

import "fmt"

//first lets create a linkedlist in golang
type Node1 struct {
	value	int
	next	*Node1
}

func NewNode1(value int) *Node1 {
	return &Node1{
		value: value,
		next: nil,
	}
}

func createLL1(arr []int) *Node1 {
	head := NewNode1(arr[0])
	v := head

	for i := 1; i < len(arr); i++ {
		v.next = NewNode1(arr[i])
		v = v.next
	}
	return head
}

func printLL1(head *Node1) {
	pointer := head

	for pointer != nil {
		fmt.Println(pointer.value)
		pointer = pointer.next
	}
}

func remNthSolution(head *Node1, n int) *Node1{
	arr := []*Node1{}

	for head != nil {
		arr = append(arr, head)
		head = head.next
	}
	
	pos := len(arr) - n

	head = arr[0]
	prev := head

	for i:=1; i < len(arr); i++ {
		if i == pos{
			prev.next = nil
			continue
		}
		prev.next = arr[i]
		prev = prev.next
	}
	return head
}




func RemoveNthFromEnd(){
	arr := []int{1,2,3,4,5}
	head := createLL1(arr)
	head = remNthSolution(head, 2)
	printLL1(head)
}