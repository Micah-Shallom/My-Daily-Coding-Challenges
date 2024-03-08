// You are given an array nums consisting of positive integers.

// Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

// The frequency of an element is the number of occurrences of that element in the array.

// Example 1:

// Input: nums = [1,2,2,3,1,4]
// Output: 4
// Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
// So the number of elements in the array with maximum frequency is 4.
// Example 2:

// Input: nums = [1,2,3,4,5]
// Output: 5
// Explanation: All elements of the array have a frequency of 1 which is the maximum.
// So the number of elements in the array with maximum frequency is 5.

package challenges

import (
	"fmt"
)

func mfeSolution(nums []int) (count int) {
	hashMap := map[int]int{}
	max_val := 0

	for _, val := range nums{
		hashMap[val]++
		max_val = max(max_val,hashMap[val])
	}
	
	for _, val := range hashMap{
		if val == max_val{
			count+=val
		}
	}
	return
}

func mfeSolution1(nums []int) int {
	hashMap := map[int]int{}
	count := 0
	max_val := 0

	for i := 0; i < len(nums); i++ {
		if _, found := hashMap[nums[i]]; found {
			hashMap[nums[i]]++
		}else{
			hashMap[nums[i]] = 1
		}
	}
	
	for _, val := range hashMap{
		max_val = max(max_val, val)
	}
	for _, val := range hashMap{
		if val == max_val{
			count+= val
		}
	}
	
	if count == 0 {
		return len(nums)
	}
	return count
}

func MaxFrequencyElements() {
	nums := []int{1,2,2,3,1,4}
	fmt.Println(mfeSolution(nums))
}
