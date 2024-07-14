// Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

// 0 <= a, b, c, d < n
// a, b, c, and d are distinct.
// nums[a] + nums[b] + nums[c] + nums[d] == target
// You may return the answer in any order.

 

// Example 1:

// Input: nums = [1,0,-1,0,-2,2], target = 0
// Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
// Example 2:

// Input: nums = [2,2,2,2,2], target = 8
// Output: [[2,2,2,2]]
 

// Constraints:

// 1 <= nums.length <= 200
// -109 <= nums[i] <= 109
// -109 <= target <= 109

package challenges

import (
	"sort"
)

func fourSum(nums []int, target int) [][]int {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})

	var res [][]int

	for i:=0; i < len(nums)-3; i++ {

		if i > 0 && nums[i] == nums[i-1] {
			continue
		}


		for j := i+1; j < len(nums)-2; j++ {
			if j > i+1 && nums[j] == nums[j-1]{
				continue
			}


			left, right := j+1, len(nums)-1

			for left < right {
				fourSum := nums[i] + nums[j] + nums[left] + nums[right]

				if fourSum == 0{
					res = append(res, []int{nums[i], nums[j], nums[left], nums[right]})

					for left < right && nums[left] == nums[left+1]{
						left++
					}
					for left < right && nums[right] == nums[right-1]{
						right--
					}
					left++
					right--
				}else if fourSum < 0{
					left++
				}else{
					right--
				}
			}
		} 
	}
	return res
}