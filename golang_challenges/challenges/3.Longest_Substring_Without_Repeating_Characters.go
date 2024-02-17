// # Given a string s, find the length of the longest
// # substring without repeating characters.
// # Example 1:

// # Input: s = "abcabcbb"
// # Output: 3
// # Explanation: The answer is "abc", with the length of 3.

// # Example 2:
// # Input: s = "bbbbb"
// # Output: 1
// # Explanation: The answer is "b", with the length of 1.

// # Example 3:
// # Input: s = "pwwkew"
// # Output: 3
// # Explanation: The answer is "wke", with the length of 3.
// # Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

package challenges

import "fmt"

func lsSolution(s string) int {
	seen, l, length := map[byte]int{}, 0, 0

	for r := 0; r < len(s); r++ {
		char := s[r]
		if index, found := seen[char]; found && index >= l {
			l = index + 1
		} else {
			length = max(length, r-l+1)
		}
		seen[char] = r
	}
	return length
}

func LengthOfLongestSubString() {
	s := "abcabcbb"
	fmt.Println(lsSolution(s))
}
