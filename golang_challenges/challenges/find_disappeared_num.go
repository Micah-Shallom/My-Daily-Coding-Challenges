// # Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

// # Example 1:
// # Input: nums = [4,3,2,7,8,2,3,1]
// # Output: [5,6]

// # Example 2:
// # Input: nums = [1,1]
// # Output: [2]
package challenges

import "fmt"


func fdsSolution(nums []int)[]int{
	hashMap := map[int]int{}
	for i:=1; i < len(nums)+1; i++ {
		hashMap[i] = 0
	}
	for i := range(nums){
		hashMap[nums[i]] += 1
	}
	var result []int
	for k, v := range hashMap{
		if v == 0{
			result = append(result, k)
		}
	}
	return result
}

func FindDisappearedNums(){
	fmt.Println(fdsSolution([]int{4,3,2,7,8,2,3,1}))
}