// # 205. Isomorphic Strings

// # Given two strings s and t, determine if they are isomorphic.

// # Two strings s and t are isomorphic if the characters in s can be replaced to get t.

// # All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

// # Example 1:

// # Input: s = "egg", t = "add"
// # Output: true
// # Example 2:

// # Input: s = "foo", t = "bar"
// # Output: false
// # Example 3:

// # Input: s = "paper", t = "title"
// # Output: true

package challenges

import "fmt"

func isIsomorphicSolution(s, t string) bool {
	if len(s) != len(t) {
		return false
	}

	mapST, mapTS := make(map[byte]byte), make(map[byte]byte)

	for i := 0; i < len(s); i++ {
		cS, cT := s[i], t[i]

		if (mapST[cS] != 0 && mapST[cS] != cT) || (mapTS[cT] != 0 && mapTS[cT] != cS) {
			return false
		}

		mapST[cS] = cT
		mapTS[cT] = cS
	}
	return true
}

func IsIsomorphic() {
	s, t := "egg", "add"
	ans := isIsomorphicSolution(s, t)
	fmt.Println(ans)
}
