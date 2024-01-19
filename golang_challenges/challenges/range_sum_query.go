// # Given an integer array nums, handle multiple queries of the following type:

// # Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
// # Implement the NumArray class:

// # NumArray(int[] nums) Initializes the object with the integer array nums.
// # int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

// # Example 1:
// # Input
// # ["NumArray", "sumRange", "sumRange", "sumRange"]
// # [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
// # Output
// # [null, 1, -1, -3]

// # Explanation
// # NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
// # numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
// # numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
// # numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

package challenges

import "fmt"

type NumArray struct{
	prefixSums []int
	curr_val	int
}

func Constructor(nums []int) NumArray {
	prefixSums := []int{}
	curr_val := 0

	for idx := range nums{
		curr_val += nums[idx]
		prefixSums = append(prefixSums, curr_val)
	}
	numConst := NumArray{
		prefixSums,
		curr_val,
	}
	return numConst
}

func (this *NumArray) sumRange(left, right int) int {
	rightSums := this.prefixSums[right]
	leftSums := 0
	if left > 0{
		leftSums = this.prefixSums[left - 1]
	}
	return rightSums - leftSums
}

func RangeSumQuery() {
	nums := []int{-2, 0, 3, -5, 2, -1}
	vals := Constructor(nums)
	result := vals.sumRange(0, 5)
	fmt.Println(result)
}