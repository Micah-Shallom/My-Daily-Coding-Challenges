// Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

// The following rules define a valid string:

// Any left parenthesis '(' must have a corresponding right parenthesis ')'.
// Any right parenthesis ')' must have a corresponding left parenthesis '('.
// Left parenthesis '(' must go before the corresponding right parenthesis ')'.
// '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

// Example 1:

// Input: s = "()"
// Output: true
// Example 2:

// Input: s = "(*)"
// Output: true
// Example 3:

// Input: s = "(*))"
// Output: true

// Constraints:

// 1 <= s.length <= 100
// s[i] is '(', ')' or '*'.

package challenges

import "fmt"

func cvpSolution(s string)bool{
	open := 0
	openMax := 0 

	for _, char := range s {
		switch char{
			case '(':
				open++
				openMax++
			case ')':
				open--
				openMax--
			default:
				open--
				openMax++
		}
		if openMax < 0{
			return false
		}
		if open < 0{
			open = 0
		}
	}
	return open == 0
}

func CheckValidParenthesis(){
	s := "(**"
	fmt.Println(cvpSolution(s))
}