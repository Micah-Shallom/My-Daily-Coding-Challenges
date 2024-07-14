// You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

// Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

// Example 1:

// Input: s = "ABAB", k = 2
// Output: 4
// Explanation: Replace the two 'A's with two 'B's or vice versa.
// Example 2:

// Input: s = "AABABBA", k = 1
// Output: 4
// Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
// The substring "BBBB" has the longest repeating letters, which is 4.
// There may exists other ways to achieve this answer too.

package challenges

func characterReplacement(s string,  k int) int{
	maxCount := 0
	maxLen := 0
	left := 0


	m := make(map[byte]int)

	for right := 0 ; right<len(s); right++{
		r_char := s[right]

		m[r_char]++
		maxCount = max(maxCount, m[r_char])

		if (right - left + 1) - maxCount > k {
			l_char := s[left]
			m[l_char]--
			left++
		}

		maxLen = max(maxLen, right - left + 1)
	}
	return maxLen
}