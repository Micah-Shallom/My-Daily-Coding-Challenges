//

package challenges

func longestPalindrome(s string) int {
	charCount := make(map[rune]int)

	//create a hasmap of characters and their counts
	for _, char := range s {
		charCount[char]++
	}

	palindromeLength := 0
	odd := false
	for _, count := range charCount {
		if count%2 == 0 {
			palindromeLength += count
		} else {
			palindromeLength += count - 1
			odd = true
		}
	}
	if odd {
		palindromeLength++
	}
	return palindromeLength
}
