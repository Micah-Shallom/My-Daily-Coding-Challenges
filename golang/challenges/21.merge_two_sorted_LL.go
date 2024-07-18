package challenges

import (
	"fmt"

)

type Node struct {
	value int
	next  *Node
}

func NewNode(value int) *Node {
	return &Node{
		value: value,
		next:  nil,
	}
}

func createLL(arr []int) *Node {
	head := NewNode(arr[0])
	x := head

	for i := 1; i < len(arr); i++ {
		x.next = NewNode(arr[i])
		x = x.next
	}
	return head
}

func mergeLL(head1 *Node, head2 *Node) *Node {
	dummyNode := NewNode(0)

	tail := dummyNode

	for {
		if head1 == nil {
			tail.next = head2
			break
		}
		if head2 == nil {
			tail.next = head1
			break
		}

		if head1.value <= head2.value{
			tail.next = head1
			head1 = head1.next
		}else{
			tail.next = head2
			head2 = head2.next
		}

		tail = tail.next
	}

	return dummyNode.next
}

func printLL(head *Node) {
	pointer := head

	for pointer != nil {
		fmt.Println(pointer.value)
		pointer = pointer.next
	}
}

func MergeTwoLL() {
	arr1 := []int{1, 2, 4}
	arr2 := []int{1, 3, 4}
	head1, head2 := createLL(arr1), createLL(arr2)
	mergedHead := mergeLL(head1, head2)
	printLL(mergedHead)
}