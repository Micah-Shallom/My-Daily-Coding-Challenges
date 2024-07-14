// Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

// A subarray is a contiguous part of the array.

// Example 1:
// Input: nums = [1,0,1,0,1], goal = 2
// Output: 4
// Explanation: The 4 subarrays are bolded and underlined below:
// [1,0,1,0,1]
// [1,0,1,0,1]
// [1,0,1,0,1]
// [1,0,1,0,1]

// Example 2:
// Input: nums = [0,0,0,0,0], goal = 0
// Output: 15

package challenges

import "fmt"

func nswsSolution(nums []int, goal int) int {
	
	// lp := 0
	// winSum := 0
	// count := 0
	// rp := 1
	// winSum += nums[lp] //add the first element in nums

	// for lp < rp{

	// 	if rp == len(nums){
	// 		rp = len(nums)
	// 	}

	// 	if winSum < goal{
	// 		winSum += nums[rp]
	// 		rp++
	// 	}else if winSum > goal {
	// 		lp++
	// 		winSum -= nums[lp]
	// 	}else{
	// 		count++
	// 	}
	// 	fmt.Println(winSum)
	// }

	// return count

		count := 0
		currentSum := 0
		left := 0
	  
		for right := range nums {
		  // Add the current element to the window sum
		  currentSum += nums[right]
	  
		  // Slide the left pointer until the window sum becomes less than or equal to the goal
		  for currentSum > goal {
			currentSum -= nums[left]
			left++

			if currentSum == goal {
				count++
			}
		  }
	  
		  // If the window sum equals the goal, increment the count for valid subarrays
		  if currentSum == goal {
			count++
		  }
		}
	  
		return count
	  

}

func NumSubarraysWithSum(){
	nums := []int{1,0,1,0,1}
	goal := 2
	fmt.Println(nswsSolution(nums, goal))
}