// Given the root of a binary tree, return the inorder traversal of its nodes' values.
// Example 1:
// Input: root = [1,null,2,3]
// Output: [1,3,2]
// Example 2:

// Input: root = []
// Output: []
// Example 3:

// Input: root = [1]
// Output: [1]

package challenges

import "fmt"

type TreeNode struct{
	Val int
	Left *TreeNode
	Right *TreeNode
}

func NewTreeNode(val int) *TreeNode{
	return &TreeNode{
		Val: val,
		Left: nil,
		Right: nil,
	}
}

func createTrees() *TreeNode{
	head := NewTreeNode(1)
	head.Left = NewTreeNode(2)
	head.Right = NewTreeNode(3)

	return head
}

func iotSolution(root *TreeNode) []int{
	res := []int{}

	var dfs func(*TreeNode)

	dfs = func(root *TreeNode){
		if root != nil {
			dfs(root.Left)
			res = append(res, root.Val)
			dfs(root.Right)
		}
	}
	dfs(root)
	return res
}


func InOrderTraversal() {
	head := createTrees()
	fmt.Println(iotSolution(head))
}