// You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

// If isLefti == 1, then childi is the left child of parenti.
// If isLefti == 0, then childi is the right child of parenti.
// Construct the binary tree described by descriptions and return its root.

// The test cases will be generated such that the binary tree is valid.

 

// Example 1:


// Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
// Output: [50,20,80,15,17,19]
// Explanation: The root node is the node with value 50 since it has no parent.
// The resulting binary tree is shown in the diagram.
// Example 2:


// Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
// Output: [1,2,null,null,3,4]
// Explanation: The root node is the node with value 1 since it has no parent.
// The resulting binary tree is shown in the diagram.
package challenges

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func createBinaryTree(desc [][]int) *TreeNode {
    hashT := make(map[int]*TreeNode)
    cpMap := make(map[int]bool)

    for _, v := range desc{
        p, c , d := v[0], v[1], v[2]

        if _, ex := hashT[p]; !ex{
            hashT[p] = &TreeNode{Val: p}
        }
        if _, ex := hashT[c]; !ex{
            hashT[c] = &TreeNode{Val: c}
        }

        pN, cN := hashT[p], hashT[c]
        if d == 1 {
            pN.Left = cN
        }else{
            pN.Right = cN
        }

        cpMap[c] = true
    }

    for _, v := range desc{
        if _, ex := cpMap[v[0]]; !ex {
            return hashT[v[0]]
        }
    }
    return nil
}