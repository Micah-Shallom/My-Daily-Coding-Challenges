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
	left := 0
	product := 1

	for right := 0; right < len(nums); right ++ {
		product *= nums[right]

		for product >= k && left <= right {
			product /= nums[left]
			left++
		}
		count += right - left + 1
	}
	return count
}

func NumSubArrayProduct(){
	arr := []int{10,2,5,6}
	k := 100
	fmt.Println(numSubarrayProductLessThanK(arr,k))
}