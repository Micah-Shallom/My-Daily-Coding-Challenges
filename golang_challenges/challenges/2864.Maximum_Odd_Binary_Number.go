// You are given a binary string s that contains at least one '1'.

// You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

// Return a string representing the maximum odd binary number that can be created from the given combination.

// Note that the resulting string can have leading zeros.

// Example 1:

// Input: s = "010"
// Output: "001"
// Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".
// Example 2:

// Input: s = "0101"
// Output: "1001"
// Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".

// Constraints:

// 1 <= s.length <= 100
// s consists only of '0' and '1'.
// s contains at least one '1'.

package challenges

import (
	"fmt"
	"sort"
	"strings"
)

func mobmSolution(s string) string{
	characters := strings.Split(s, "")
	sort.Strings(characters)
	
	s = strings.Join(characters, "")
	result := reverseStrings(s[:len(s)- 1])+s[len(s)-1:]

	return result
}

func reverseStrings(s string) string{
	l, r := 0, len(s)-1

	char := strings.Split(s, "")


	for l< r {
		char[l], char[r] = char[r], char[l]
		l++
		r--
	}
	return strings.Join(char,"")
}


func MaximumOddBinaryNumber() {
	s := "0101"
	fmt.Println(mobmSolution(s))
}