package algorithms

import (
	"fmt"
)

type TreeNode struct {
	Value int
	Left  *TreeNode
	Right *TreeNode
}

func Insert(root *TreeNode, value int) *TreeNode {
	if root == nil {
		return &TreeNode{
			Value: value,
		}
	}

	if value <= root.Value {
		root.Left = Insert(root.Left, value)
	} else {
		root.Right = Insert(root.Right, value)
	}
	return root
}

func CreateTree(arr []int) *TreeNode {
	var root *TreeNode

	for i := range arr {
		if arr[i] != -1 {
			root = Insert(root, arr[i])
		}
	}
	return root
}

func PrintTree(root *TreeNode) {
	if root == nil {
		return
	}

	fmt.Print(root.Value, " ")
	PrintTree(root.Left)
	PrintTree(root.Right)
}

func main() {
	arr := []int{4, 1, 6, 0, 2, 5, 7, -1, -1, -1, 3, -1, -1, -1, 8}
	root := CreateTree(arr)
	PrintTree(root)
}
