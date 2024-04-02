// You are given an integer array nums and an integer k.

// The frequency of an element x is the number of times it occurs in an array.

// An array is called good if the frequency of each element in this array is less than or equal to k.

// Return the length of the longest good subarray of nums.

// A subarray is a contiguous non-empty sequence of elements within an array.

// Example 1:

// Input: nums = [1,2,3,1,2,3,1,2], k = 2
// Output: 6
// Explanation: The longest possible good subarray is [1,2,3,1,2,3] since the values 1, 2, and 3 occur at most twice in this subarray. Note that the subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.
// It can be shown that there are no good subarrays with length more than 6.
// Example 2:

// Input: nums = [1,2,1,2,1,2,1,2], k = 1
// Output: 2
// Explanation: The longest possible good subarray is [1,2] since the values 1 and 2 occur at most once in this subarray. Note that the subarray [2,1] is also good.
// It can be shown that there are no good subarrays with length more than 2.
// Example 3:

// Input: nums = [5,5,5,5,5,5,5], k = 4
// Output: 4
// Explanation: The longest possible good subarray is [5,5,5,5] since the value 5 occurs 4 times in this subarray.
// It can be shown that there are no good subarrays with length more than 4.

package challenges

import "fmt"

func maxSubarrayLength(nums []int, k int) int {
	count := 0
	left := 0
	hashMap := make(map[int]int)

	for right, num := range nums {
		hashMap[num]++

		for hashMap[num] > k {
			hashMap[nums[left]]--
			left++
		}
		count = max(count, right-left+1)
	}
	
	return count
}


func MaxSubLength() {
	nums := []int{1,2,3,1,2,3,1,2}
	k := 2
	fmt.Println(maxSubarrayLength(nums, k))
}
