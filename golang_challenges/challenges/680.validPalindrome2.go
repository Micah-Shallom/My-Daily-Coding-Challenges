// # Given a string s, return true if the s can be palindrome after deleting at most one character from it.

// # Example 1:

// # Input: s = "aba"
// # Output: true
// # Example 2:

// # Input: s = "abca"
// # Output: true
// # Explanation: You could delete the character 'c'.
// # Example 3:

// # Input: s = "abc"
// # Output: false

package challenges

import "fmt"

func reverseString(s string) string {
	runes := []rune(s)

	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}


func vpSolution(s string) bool {
	l, r := 0, len(s)-1

	for l < r {
		if s[l] != s[r] {
			skipL, skipR := s[l+1:r+1], s[l:r]
			return skipL == reverseString(skipL) || skipR == reverseString(skipR)
		}
		l, r = l+1, r-1
	}
	return true
}

func ValidPalindrome() {
	s := "abcda"
	ans := vpSolution(s)
	fmt.Println(ans)
}
