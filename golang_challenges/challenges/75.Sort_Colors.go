// Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

// We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

// You must solve this problem without using the library's sort function.

 

// Example 1:

// Input: nums = [2,0,2,1,1,0]
// Output: [0,0,1,1,2,2]
// Example 2:

// Input: nums = [2,0,1]
// Output: [0,1,2]


package challenges

func sortColors(nums []int){
	hm := make(map[int]int)

	for _, v := range nums {
		hm[v]++
	}

	idx := 0
	for i :=0; i < 3; i++{
		v := hm[i]

		for v > 0 {
			nums[idx] = i
			idx++
			v--
			hm[i]--
		}
	}
}

//using bubblesort algorithm

func sortColors(nums []int) {
	for i := 0; i < len(nums) - 1 ; i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] > nums[j]{
				nums[i], nums[j] = nums[j] , nums[i]
			}
		}
	}
}