// Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

// Example 1:

// Input: nums = [0,1]
// Output: 2
// Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
// Example 2:

// Input: nums = [0,1,0]
// Output: 2
// Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
package challenges

import "fmt"

func findmaxSolution(nums []int) int {
	zeros, ones := 0, 0
	hashmap := make(map[int]int)
	res := 0

	for i := 0; i < len(nums); i++ {
		if nums[i] == 0{
			zeros++
		}else{
			ones++
		}

		diff := ones - zeros
		if _, exists := hashmap[diff]; !exists{
			hashmap[diff] = i
		}

		if ones == zeros {
			res = i + 1
		}else{
			res = max(res, i - hashmap[diff])
		}

	}
	
	return res
}

func FindMaxLength(){
	// nums := []int{0,1,0}
	nums := []int{1,1,1,0,0,0,0,0,1}
	fmt.Println(findmaxSolution(nums))
}