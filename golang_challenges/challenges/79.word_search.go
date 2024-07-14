// // Given an m x n grid of characters board and a string word, return true if word exists in the grid.

// // The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

// // Example 1:


// // Input: board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = 'ABCCED'
// // Output: true
// // Example 2:


// // Input: board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = 'SEE'
// // Output: true
// // Example 3:


// // Input: board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = 'ABCB'
// // Output: false
 

// // Constraints:

// // m == board.length
// // n = board[i].length
// // 1 <= m, n <= 6
// // 1 <= word.length <= 15
// // board and word consists of only lowercase and uppercase English letters.

package challenges

// import "fmt"

// func wsSolution(board [][]byte, word string) bool {
// 	rows := len(board)
// 	cols := len(board[0])
	
// 	for i := 0; i < rows; i++ {
// 		for j := 0; j < cols; j++{
// 			if board[i][j] == word[0]{
// 				rs := dfs(board, i , j , 0, word)

// 				if rs {
// 					return true
// 				}
// 			}
// 		}
// 	}
// 	return false
// }

// func dfs(board [][]byte, i , j, pos int, word string) bool {

// }

// func WordSearch(){
// 	board := [][]byte{{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}}
// 	word := "ABCCED"
// 	fmt.Println(wsSolution(board, word))
// }