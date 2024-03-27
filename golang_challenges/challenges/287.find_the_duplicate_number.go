// Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

// There is only one repeated number in nums, return this repeated number.

// You must solve the problem without modifying the array nums and uses only constant extra space.
// Example 1:

// Input: nums = [1,3,4,2,2]
// Output: 2

// Example 2:
// Input: nums = [3,1,3,4,2]
// Output: 3

// Example 3:
// Input: nums = [3,3,3,3,3]
// Output: 3
package challenges

import (
	"fmt"
	// "sort"
)

func fdSolution(nums []int) int {
    slow := nums[0]
	fast := nums[0]

	for {
		slow = nums[slow]
		fast = nums[nums[fast]]
		if slow == fast{
			return slow
		}
	}
	return 0

	// sort.Slice(nums, func(i, j int)  bool {
	// 	return nums[i] < nums[j]
	// })
	
	// for i := 0; i < len(nums); i++ {
	// 	if nums[i] == nums[i+1]{
	// 		return nums[i]
	// 	}
	// }
	// return 0
}

func FindDuplicate(){
	fmt.Println(fdSolution([]int{3,1,3,4,2}))
}