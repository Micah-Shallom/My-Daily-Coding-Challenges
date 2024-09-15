// Given the root of a binary tree, return all root-to-leaf paths in any order.

// A leaf is a node with no children.

 

// Example 1:


// Input: root = [1,2,3,null,5]
// Output: ["1->2->5","1->3"]
// Example 2:

// Input: root = [1]
// Output: ["1"]

package challenges


func binaryTreePaths(root *TreeNode) []string {
	var res []string
	var dfs func(root *TreeNode, path string)
	
	dfs = func(root *TreeNode, path string) {
		if root == nil {
			return
		}
		
		path += strconv.Itoa(root.Val)
		
		if root.Left == nil && root.Right == nil {
			res = append(res, path)
			return
		}
		
		path += "->"
		dfs(root.Left, path)
		dfs(root.Right, path)
	}
	
	dfs(root, "")
	
	return res
}