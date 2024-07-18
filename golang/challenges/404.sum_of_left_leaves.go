// Given the root of a binary tree, return the sum of all left leaves.

// A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

// Example 1:

// Input: root = [3,9,20,null,null,15,7]
// Output: 24
// Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
// Example 2:

// Input: root = [1]
// Output: 0

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 package challenges

func dfs(root *TreeNode, isLeft bool) int {
	if root == nil {
		return 0
	}

	if isLeft == true && root.Left == nil && root.Right == nil {
		return root.Val
	}

	countLeft := dfs(root.Left, true)
	countRight := dfs(root.Right, false)

	return countLeft + countRight
}

func sumOfLeftLeaves(root *TreeNode) int {
	return dfs(root, false)
}