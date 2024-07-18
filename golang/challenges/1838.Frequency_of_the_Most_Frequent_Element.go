// The frequency of an element is the number of times it occurs in an array.

// You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

// Return the maximum possible frequency of an element after performing at most k operations.

 

// Example 1:

// Input: nums = [1,2,4], k = 5
// Output: 3
// Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
// 4 has a frequency of 3.
// Example 2:

// Input: nums = [1,4,8,13], k = 5
// Output: 2
// Explanation: There are multiple optimal solutions:
// - Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
// - Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
// - Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
// Example 3:

// Input: nums = [3,9,6], k = 2
// Output: 1


package challenges

import (
	"sort"
)

func maxFrequency(nums []int, k int) int {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})

	l, r := 0, 0
	res, total := 0, 0

	for r < len(nums){
		total += nums[r]

		for nums[r] * (r - l + 1) > total + k {
			total -= nums[l]
			l++
		}

		res = max(res, (r -l + 1))
		r++

	}
	return res

}
