// Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

// Example 1:

// Input: temperatures = [73,74,75,71,69,72,76,73]
// Output: [1,1,4,2,1,1,0,0]
// Example 2:

// Input: temperatures = [30,40,50,60]
// Output: [1,1,1,0]
// Example 3:

// Input: temperatures = [30,60,90]
// Output: [1,1,0]

package challenges

import "fmt"

func dtSolution1(temp []int) []int {
	var stack []int
	ans := make([]int, len(temp))
	for i := 0; i < len(temp); i++ {
		for len(stack) > 0 && temp[stack[len(stack)-1]] < temp[i] {
			j := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			ans[j] = i - j
		} 
		stack = append(stack, i)
	}
	return ans
}

func dtSolution(temp []int) []int {
	stack := make([]int, len(temp))
	l, r := 0, 1

	count := 0
	for l < len(temp) {
		if temp[r] < temp[l] {
			r += 1
			count += 1
		} else {
			stack[l] = count
			l += 1
			r = l + 1
			count = 0
		}
	}
	return stack
}

func DailyTemperatures() {
	temperatures := []int{73, 74, 75, 71, 69, 72, 76, 73}
	fmt.Println(dtSolution1(temperatures))
}
