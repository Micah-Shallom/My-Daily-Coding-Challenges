// Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

// Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
// Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
// The prefix and the suffix should not intersect at any index.
// The characters from the prefix and suffix must be the same.
// Delete both the prefix and the suffix.
// Return the minimum length of s after performing the above operation any number of times (possibly zero times).

// Example 1:

// Input: s = "ca"
// Output: 2
// Explanation: You can't remove any characters, so the string stays as is.
// Example 2:

// Input: s = "cabaabac"
// Output: 0
// Explanation: An optimal sequence of operations is:
// - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
// - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
// - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
// - Take prefix = "a" and suffix = "a" and remove them, s = "".
// Example 3:

// Input: s = "aabccabba"
// Output: 3
// Explanation: An optimal sequence of operations is:
// - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
// - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
package challenges

import "fmt"

func minimumLsolution(s string) int {
	l, r := 0, len(s)-1

	for l < r && s[l] == s[r]{

		hold := s[l]
		for l <= r && hold == s[l] {
			l++
		}
		for l <= r && hold == s[r] {
			r--
		}
	}
	return r - l + 1
}

// func minimumLsolution(s string) int {
//     left, right := 0, len(s)-1

//     for left < right {
// 		if s[left] != s[right]{
// 			return right - left + 1
// 		}

// 		if s[left+1] == s[left] && s[left] == s[right]{
// 			left++
// 			continue
// 		}
// 		if s[right-1] == s[right] && s[left] == s[right]{
// 			right--
// 			continue
// 		}
//         if s[left] == s[right] {
// 			left++
//             right--
// 			} else {
// 				break
// 		}
//     }

// 	fmt.Println(left, right)
// 	if left == right && s[left] == s[right] {
// 		return 1
// 	}

//     if left >= right  {
//         return 0
//     }

//     return right - left + 1
// }

func MinimumLength() {
	s := "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"
	fmt.Println(minimumLsolution(s))
}
