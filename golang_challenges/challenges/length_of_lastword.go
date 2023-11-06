// # Given a string s consisting of words and spaces, return the length of the last word in the string.
// # A word is a maximal
// # substring
package challenges

import "fmt"

// #  consisting of non-space characters only.

// # Example 1:
// # Input: s = "Hello World"
// # Output: 5
// # Explanation: The last word is "World" with length 5.

// # Example 2:
// # Input: s = "   fly me   to   the moon  "
// # Output: 4
// # Explanation: The last word is "moon" with length 4.

// # Example 3:
// # Input: s = "luffy is still joyboy"
// # Output: 6
// # Explanation: The last word is "joyboy" with length 6.

// # Constraints:
// # 1 <= s.length <= 104
// # s consists of only English letters and spaces ' '.
// # There will be at least one word in s.

func llwsolution(s string) int{
	count := 0 
	for i :=len(s)-1; i  >= 0 ; i--{
		if s[i] != ' '{
			count += 1
		}
		if count !=0 && s[i] == ' '{
			break
		}
	}
	return count
}

func LengthLastWord(){
	str := "   fly me   to   the moon  "
	ans := llwsolution(str)
	fmt.Println(ans)
}