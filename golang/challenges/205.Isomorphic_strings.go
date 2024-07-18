// Given two strings s and t, determine if they are isomorphic.

// Two strings s and t are isomorphic if the characters in s can be replaced to get t.

// All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

// Example 1:

// Input: s = "egg", t = "add"
// Output: true
// Example 2:

// Input: s = "foo", t = "bar"
// Output: false
// Example 3:

// Input: s = "paper", t = "title"
// Output: true

package challenges

import "fmt"

func iisolution(s , t string) (res bool) {
	// s_to_t := make(map[rune]string)
	// t_to_s := make(map[rune]string)

	// for idx, s_val := range s{
	// 	if key, exists := s_to_t[s_val]; exists{
	// 		if key != string(t[idx]){
	// 			return false
	// 		}
	// 	}else{
	// 		s_to_t[s_val] = string(t[idx])
	// 	}
	// }

	// for idx, t_val := range t {
	// 	if key, exists := t_to_s[t_val]; exists{
	// 		if key != string(s[idx]) {
	// 			return false
	// 		}
	// 	}else{
	// 		t_to_s[t_val] = string(s[idx])
	// 	}
	// }

	// return true	
	sPattern, tPattern := map[uint8]int{}, map[uint8]int{}
	for index := range s {
		if sPattern[s[index]] != tPattern[t[index]]{
			return false
		}else{
			sPattern[s[index]] = index + 1
			tPattern[t[index]] = index + 1
		}
	}
	fmt.Println(sPattern, tPattern)
	return true
}

func IsIsomorphic(){
	s := "egg"
	t := "add"
	fmt.Println(iisolution(s, t))
}