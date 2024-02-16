// # You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

// # Return the merged string.
// # Example 1:

// # Input: word1 = "abc", word2 = "pqr"
// # Output: "apbqcr"
// # Explanation: The merged string will be merged as so:
// # word1:  a   b   c
// # word2:    p   q   r
// # merged: a p b q c r

// # Example 2:
// # Input: word1 = "ab", word2 = "pqrs"
// # Output: "apbqrs"
// # Explanation: Notice that as word2 is longer, "rs" is appended to the end.
// # word1:  a   b
// # word2:    p   q   r   s
// # merged: a p b q   r   s

// # Example 3:
// # Input: word1 = "abcd", word2 = "pq"
// # Output: "apbqcd"
// # Explanation: Notice that as word1 is longer, "cd" is appended to the end.
// # word1:  a   b   c   d
// # word2:    p   q
// # merged: a p b q c   d
package challenges

import "fmt"

func maSolution(word1, word2 string) string {
	res := []rune{}

	i, j := 0, 0

	for i < len(word1) && j < len(word2) {
		res = append(res, rune(word1[i]))
		res = append(res, rune(word2[j]))
		i++
		j++
	}

	for i < len(word1) {
		res = append(res, rune(word1[i]))
		i++
	}

	for j < len(word2) {
		res = append(res, rune(word2[j]))
		j++
	}

	return string(res)
}

func MergeAlternately() {
	word1, word2 := "abc", "pqr"
	fmt.Println(maSolution(word1, word2))
}
