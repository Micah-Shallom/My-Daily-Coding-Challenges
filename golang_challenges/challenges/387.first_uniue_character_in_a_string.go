// # Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

// # Example 1:

// # Input: s = "leetcode"
// # Output: 0
// # Example 2:

// # Input: s = "loveleetcode"
// # Output: 2
// # Example 3:

// # Input: s = "aabb"
// # Output: -1
package challenges

import "fmt"

func fuSolution(s string) int {
	count := map[rune]int{}

	for _, c := range s {
		count[c]++
	}

	for i, c := range s {
		if count[c] == 1 {
			return i
		}
	}
	return -1
}

func FirstUnique() {
	s := "loveleetcode"
	fmt.Println(fuSolution(s))
}
