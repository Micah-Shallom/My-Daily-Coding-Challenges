// Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

// In other words, return true if one of s1's permutations is the substring of s2.

 

// Example 1:

// Input: s1 = "ab", s2 = "eidbaooo"
// Output: true
// Explanation: s2 contains one permutation of s1 ("ba").
// Example 2:

// Input: s1 = "ab", s2 = "eidboaoo"
// Output: false
 

// Constraints:

// 1 <= s1.length, s2.length <= 104
// s1 and s2 consist of lowercase English letters.


package challenges

func checkInclusion(s1 string, s2 string) bool {
	if len(s1) > len(s2){
		return false
	}

	m1 := make(map[byte]int)
	m2 := make(map[byte]int)

	for i:=0; i<len(s1); i++{
		m1[s1[i]]++
		m2[s2[i]]++
	}

	if equals := mapequals(m1, m2); equals{
		return true
	}

	for i:=len(s1); i<len(s2); i++ {
		m2[s2[i]]++
		m2[s2[i-len(s1)]]--

		if m2[s2[i-len(s1)]] == 0{
			delete(m2, s2[i-len(s1)])
		}

		if equals := mapequals(m1, m2); equals {
			return true
		}
	}
	return false

}

type dictype map[byte]int
func mapequals(m1, m2 dictype) bool {
	if len(m1) != len(m2){
		return false
	}

	for k , v := range m1 {
		if v2, exists := m2[k]; !exists || v != v2 {
			return false
		}
	}
	return true
}