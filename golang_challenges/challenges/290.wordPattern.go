// # Given a pattern and a string s, find if s follows the same pattern.

// # Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

// # Example 1:

// # Input: pattern = "abba", s = "dog cat cat dog"
// # Output: true
// # Example 2:

// # Input: pattern = "abba", s = "dog cat cat fish"
// # Output: false
// # Example 3:

// # Input: pattern = "aaaa", s = "dog cat cat dog"
// // # Output: false

package challenges

import (
	"fmt"
	"strings"
)


func wpSolution(p , s string) bool{
	word := strings.Split(s," ")
	if len(p) != len(word){
		return false
	}
	
	charToWord := map[string]string{}
	wordToChar := map[string]string{}
	
	for i:=0; i< len(p); i++{
		c := string(p[i])
		w := word[i]

		if _, exists := charToWord[c]; exists{
			if charToWord[c] != w {
				return false
			}
		}
		charToWord[c] = w

		if _, exists := wordToChar[w]; exists{
			if wordToChar[w] != c {
				return false
			}
		}
		wordToChar[w] = c
	}
	fmt.Println(charToWord,wordToChar)
	return true
}


func WordPattern(){
	pattern := "abbc"
	s := "dog cat cat dog"
	fmt.Println(wpSolution(pattern,s))
}