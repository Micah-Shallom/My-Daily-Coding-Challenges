// iven two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

// Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

// Example 1:

// Input: nums1 = [1,2,3], nums2 = [2,4]
// Output: 2
// Explanation: The smallest element common to both arrays is 2, so we return 2.
// Example 2:

// Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
// Output: 2
// Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
package challenges

import "fmt"

func gcSolution(nums1 []int, nums2 []int) (int) {
	p1 := 0
	p2 := 0

	for p1 < len(nums1) && p2 < len(nums2){
		if nums1[p1] == nums2[p2]{
			return nums1[p1]
		}else if nums1[p1] < nums2[p2]{
			p1++
		}else{
			p2++
		}
	}
	return -1
}

func GetCommon(){
	nums1 := []int{1,2,3} 
	nums2 := []int{2,4}

	fmt.Println(gcSolution(nums1, nums2))
}