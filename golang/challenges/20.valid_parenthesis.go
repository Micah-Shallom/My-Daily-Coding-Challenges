// # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// # An input string is valid if:

// # Open brackets must be closed by the same type of brackets.
// # Open brackets must be closed in the correct order.
// # Every close bracket has a corresponding open bracket of the same type.

// # Example 1:

// # Input: s = "()"
// # Output: true
// # Example 2:

// # Input: s = "()[]{}"
// # Output: true
// # Example 3:

// # Input: s = "(]"
// # Output: false

package challenges

import "fmt"

func vpthSolution(s string) bool{
	stack := []string{}
	mapping := map[string]string{")": "(", "]": "[", "}": "{"}

	for _, char := range s{
		if val, ok := mapping[string(char)]; ok{
			if len(stack) == 0 || stack[len(stack)-1] != mapping[val]{
				return false
			}
			stack = stack[:len(stack)-1]
		}else{
			stack = append(stack, string(char))
		}
	}
	return len(stack) == 0
}

func ValidParenthesis(){

	s := "()[]{}"	
	ans := vpthSolution(s)
	fmt.Println(ans)
}