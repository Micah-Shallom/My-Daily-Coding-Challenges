package algorithms

import "fmt"

type MonotonicStack struct {
	stack []int
}

func NewMonotonicStack() *MonotonicStack {
	return &MonotonicStack{
		stack: []int{},
	}
}

func (ms *MonotonicStack) Push(val int) {
	if len(ms.stack) > 0 && val > ms.stack[len(ms.stack)-1] {
		ms.pop()
	}
	ms.stack = append(ms.stack, val)
}

func (ms *MonotonicStack) pop() int {
	if len(ms.stack) == 0 {
		return -1
	}
	val := ms.stack[len(ms.stack)-1]
	ms.stack = ms.stack[:len(ms.stack)-1]
	return val
}

func (ms *MonotonicStack) peek() int {
	if len(ms.stack) == 0 {
		return -1
	}
	return ms.stack[len(ms.stack)-1]
}

func MSStack() {
	newms := NewMonotonicStack()
	newms.Push(3)
	newms.Push(2)
	newms.Push(1)
	fmt.Println(newms.stack)
}