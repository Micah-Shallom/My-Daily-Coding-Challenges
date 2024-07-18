// You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

// Evaluate the expression. Return an integer that represents the value of the expression.

// Note that:

// The valid operators are '+', '-', '*', and '/'.
// Each operand may be an integer or another expression.
// The division between two integers always truncates toward zero.
// There will not be any division by zero.
// The input represents a valid arithmetic expression in a reverse polish notation.
// The answer and all the intermediate calculations can be represented in a 32-bit integer.

// Example 1:

// Input: tokens = ["2","1","+","3","*"]
// Output: 9
// Explanation: ((2 + 1) * 3) = 9
// Example 2:

// Input: tokens = ["4","13","5","/","+"]
// Output: 6
// Explanation: (4 + (13 / 5)) = 6
// Example 3:

// Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
// Output: 22
// Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
// = ((10 * (6 / (12 * -11))) + 17) + 5
// = ((10 * (6 / -132)) + 17) + 5
// = ((10 * 0) + 17) + 5
// = (0 + 17) + 5
// = 17 + 5
// = 22s

package challenges

import "strconv"

func evalRPN(tokens []string) int {
	stack := []int{}

	for _, v := range tokens {
		//try to convert into an int, if it fails then it is an operator
		intVal, err := strconv.Atoi(v)
		if err != nil {
			//pop the last 2 elements from the stack
			x, y := stack[len(stack)-1], stack[len(stack)-2]
			stack = stack[:len(stack)-2]
			val := operation(v, x, y)
			stack = append(stack, val)
		} else {
			stack = append(stack, intVal)
		}
	}
	return stack[0]
}

func operation(sign string, x, y int) int {
	val := 0
	switch sign {
	case "+":
		val = y + x
	case "-":
		val = y - x
	case "*":
		val = y * x
	case "/":
		val = y / x
	}
	return val
}
