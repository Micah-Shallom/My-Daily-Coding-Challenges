// You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

// Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

// 'L' means to go from a node to its left child node.
// 'R' means to go from a node to its right child node.
// 'U' means to go from a node to its parent node.
// Return the step-by-step directions of the shortest path from node s to node t.

// Example 1:

// Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
// Output: "UURL"
// Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
// Example 2:

// Input: root = [2,1], startValue = 2, destValue = 1
// Output: "L"
// Explanation: The shortest path is: 2 → 1.

package challenges

import "strings"

func getDirections(root *TreeNode, startValue int, destValue int) string {
	var path []string
	var dfs func(*TreeNode) bool
	dfs = func(node *TreeNode) bool {
		if node == nil {
			return false
		}
		if node.Val == startValue {
			return true
		}
		if dfs(node.Left) || dfs(node.Right) {
			path = append(path, "L")
			return true
		}
		return false
	}
	dfs(root)
	var dfs2 func(*TreeNode) bool
	dfs2 = func(node *TreeNode) bool {
		if node == nil {
			return false
		}
		if node.Val == destValue {
			return true
		}
		if dfs2(node.Left) || dfs2(node.Right) {
			path = append(path, "R")
			return true
		}
		return false
	}
	dfs2(root)
	var dfs3 func(*TreeNode) bool
	dfs3 = func(node *TreeNode) bool {
		if node == nil {
			return false
		}
		if (node.Left != nil && node.Left.Val == startValue) || (node.Right != nil && node.Right.Val == startValue) {
			return true
		}
		if dfs3(node.Left) || dfs3(node.Right) {
			path = append(path, "U")
			return true
		}
		return false
	}
	dfs3(root)
	return strings.Join(path, "")
}
