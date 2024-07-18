package challenges

import "fmt"

// # Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

// # A string is palindromic if it reads the same forward and backward.

func reverse(word string) string{
	new_word := ""
	for i := len(word)-1; i >= 0; i--{
		new_word += string(word[i])
	}
	return new_word
}

func fPSolution(words []string) string{
	for _, word := range words{
		if word == reverse(word){
			return word
		}
	}
	return ""
}

func FirstPalindrome(){
	words := []string{"abc","car","ada","racecar","cool"}

	fmt.Println(fPSolution(words))
}