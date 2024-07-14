package challenges

// import (
// 	"fmt"
// )

// type Node struct{
// 	value int
// 	next *Node
// }
// func NewNode(value int) *Node{
// 	return &Node{
// 		value: value,
// 		next: nil,
// 	}
// }
// func createLL(arr []int) *Node {
// 	head := NewNode(arr[0])
// 	v := head

// 	for i:= 1; i< len(arr); i++ {
// 		v.next = NewNode(arr[i])
// 		v = v.next
// 	}
// 	return head
// }
// func reverseSLL(head *Node) *Node{
// 	prev, next := (*Node)(nil), (*Node)(nil)
// 	curr := head

// 	for curr!= nil {
// 		next = curr.next
// 		curr.next = prev
// 		prev = curr
// 		curr = next
// 	}
// 	return prev
// }
// func printLL(head *Node) {
// 	pointer := head

// 	for pointer != nil {
// 		fmt.Println(pointer.value)
// 		pointer = pointer.next
// 	}
// }

// func ReverseLL() {
// 	arr := []int{1, 2, 3, 4, 5}
// 	head := createLL(arr)
// 	reversedHead := reverseSLL(head)
// 	printLL(head)
// 	printLL(reversedHead)
// }
