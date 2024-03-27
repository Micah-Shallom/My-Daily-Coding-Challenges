// Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

// Example 1:
// Input: nums = [10,5,2,6], k = 100
// Output: 8
// Explanation: The 8 subarrays that have product less than 100 are:
// [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
// Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

// Example 2:
// Input: nums = [1,2,3], k = 0
// Output: 0

package challenges

import "fmt"

func numSubarrayProductLessThanK(nums []int, k int) int {
    count := 0
	
	// handle situation of an element multiplied by 1
	for _, num := range nums{
		if num < k {
			count++
		}
	}

	window_size := 2

	for window_size != len(nums) + 1 {

	}

	return count
}

func NumSubArrayProduct(){
	arr := []int{10,5,2,6}
	k := 100
	fmt.Println(numSubarrayProductLessThanK(arr, k))
}