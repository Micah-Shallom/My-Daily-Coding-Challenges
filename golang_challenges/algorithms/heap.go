package algorithms

import (
	"container/heap"
	"fmt"
)

// An IntHeap is a min-heap of ints.

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push (x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop () interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}


func Heap() {
	h := &IntHeap{2,3,10}
	heap.Init(h)

	heap.Push(h, 1)
	fmt.Println((*h)[0])

	for h.Len() > 0 {
		fmt.Println(heap.Pop(h))
	}
}