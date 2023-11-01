package challenges

import (
	"fmt"
	"strings"
)

// # Given two strings s and t, return true if t is an anagram of s, and false otherwise.
// # An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// # Example 1:
// # Input: s = "anagram", t = "nagaram"
// # Output: true

// # Example 2:
// # Input: s = "rat", t = "car"
// # Output: false

// # Constraints:
// # 1 <= s.length, t.length <= 5 * 104
// # s and t consist of lowercase English letters.

func isAnagram(s string, t string) bool {
	s,t = strings.ToLower(s), strings.ToLower(t)

	if len(s) != len(t) {
		return false
	}

	unicodeArray := make([]int, 26)

	for i := 0; i < 26; i++ {
		unicodeArray[s[i] - 'a']++
	}
	for i := 0; i < 26; i++ {
		unicodeArray[t[i] - 'a']--
	}

	for each := range(unicodeArray){
		if each != 0{
			return false
		}
	}
	return true
}

func VaSolution() {
	s, t := "anagram", "nagaram"
	fmt.Println(isAnagram(s, t))
}

