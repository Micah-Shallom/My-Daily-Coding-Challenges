package challenges

import (
	"fmt"
)

// # Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

// # Return the sorted string. If there are multiple answers, return any of them.
// # Example 1:

// # Input: s = "tree"
// # Output: "eert"
// # Explanation: 'e' appears twice while 'r' and 't' both appear once.
// # So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
// # Example 2:

// # Input: s = "cccaaa"
// # Output: "aaaccc"
// # Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
// # Note that "cacaca" is incorrect, as the same characters must be together.
// # Example 3:

// # Input: s = "Aabb"
// # Output: "bbAa"
// # Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
// # Note that 'A' and 'a' are treated as two different characters.

func fSsolution(s string) string{
	count := map[rune]int{}
	bucket := map[int][]rune{}

	for _, c := range s{
		count[c]++
	}

	for c, cnt := range count{
		bucket[cnt] = append(bucket[cnt], c)
	}

	res := []rune{}
    for i := len(s); i > 0; i-- {
        for _, c := range bucket[i] {
            for j := 0; j < i; j++ {
                res = append(res, c)
            }
        }
    }
	return string(res)
}

func FrequencySort(){
	s := "tree"
	fmt.Println(fSsolution(s))
}