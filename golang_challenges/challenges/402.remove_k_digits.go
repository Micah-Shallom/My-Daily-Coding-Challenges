// Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

// Example 1:

// Input: num = "1432219", k = 3
// Output: "1219"
// Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
// Example 2:

// Input: num = "10200", k = 1
// Output: "200"
// Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
// Example 3:

// Input: num = "10", k = 2
// Output: "0"
// Explanation: Remove all the digits from the number and it is left with nothing which is 0.

package challenges

import "strings"

func removeKdigits(num string, k int) string {
    stack := []rune{}
    remains := len(num) - k

    if len(num) == k || num == ""{
        return "0"
    }

    for _, c := range num{
        for k != 0 && len(stack) > 0 && stack[len(stack)-1] > c {
            stack = stack[:len(stack) - 1]
            k--
        }
        stack = append(stack, c)
    }

    ans := strings.TrimLeft(string(stack)[:remains], "0")
    if ans == ""{
        return "0"
    }
    return ans
}