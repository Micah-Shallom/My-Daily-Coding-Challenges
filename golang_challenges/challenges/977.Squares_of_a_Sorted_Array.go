// Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

// Example 1:

// Input: nums = [-4,-1,0,3,10]
// Output: [0,1,9,16,100]
// Explanation: After squaring, the array becomes [16,1,0,9,100].
// After sorting, it becomes [0,1,9,16,100].
// Example 2:

// Input: nums = [-7,-3,2,3,11]
// Output: [4,9,9,49,121]

// Constraints:

// 1 <= nums.length <= 104
// -104 <= nums[i] <= 104
// nums is sorted in non-decreasing order.

package challenges

import "fmt"

func ssSolution(arr []int) []int{
	new_arr := []int{}

	for _, val := range arr{
		new_arr = append(new_arr, val*val)
	}
	
	for i := 0; i < len(new_arr)-1; i++ {
		for j := 0; j < len(new_arr)-i-1; j++ {
			if new_arr[j] > new_arr[j+1]{
				new_arr[j], new_arr[j+1] = new_arr[j+1], new_arr[j]
			}
		}
	}
	return new_arr
}

func SortedSquares(){
	nums := []int{-7,-3,2,3,11}
	fmt.Println(ssSolution(nums))
}