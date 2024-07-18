package algorithms

import (
	"fmt"
)

type Node struct {
	data int
	next *Node
}

type LinkedList struct {
	head *Node
}

// func (ll *LinkedList) InsertEnd(value int) {
// 	newNode := &Node{
// 		data: value,
// 		next: nil,
// 	}

// 	if ll.head == nil {
// 		ll.head = newNode
// 	}

// 	current := ll.head

// 	for current.next != nil {
// 		current = current.next
// 	}
// 	current.next = newNode
// }

// func (ll *LinkedList) InsertBegin(data int) {
// 	newNode := &Node{
// 		data: data,
// 		next: ll.head,
// 	}

// 	ll.head = newNode
// }

func (ll *LinkedList) Insert(data, location int) {
	newNode := &Node{
		data: data,
		next: nil,
	}

	if location == 0 {
		//inserting at the beginning of the linkedlist
		newNode.next = ll.head
		ll.head = newNode
	} else if location == 1 {
		//inserting at the end of the linkedlist
		if ll.head == nil {
			ll.head = newNode
		}

		current := ll.head
		for current.next != nil {
			current = current.next
		}
		current.next = newNode
	} else {
		//insert at an index between the beginning and end of the linkedlist
		index := 0
		current := ll.head

		for index < location {
			current = current.next
			index++
		}
		tempNode := current.next
		newNode.next = tempNode
		current.next = newNode
	}
}

func (ll *LinkedList) Display() {
	current := ll.head

	for current.next != nil {
		fmt.Print(current.data, " -> ")
		current = current.next
	}

}
