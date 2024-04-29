// Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

// You must write an algorithm that runs in O(n) time and without using the division operation.

 

// Example 1:

// Input: nums = [1,2,3,4]
// Output: [24,12,8,6]
// Example 2:

// Input: nums = [-1,1,0,-3,3]
// Output: [0,0,9,0,0]
 

// Constraints:

// 2 <= nums.length <= 105
// -30 <= nums[i] <= 30
// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

// Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
package challenges

func productExceptSelf(nums []int) []int {
	n := len(nums)
	left := make([]int, n)
	right := make([]int, n)
	left[0] = 1
	right[n-1] = 1
	for i := 1; i < n; i++ {
		left[i] = left[i-1] * nums[i-1]
	}
	for i := n - 2; i >= 0; i-- {
		right[i] = right[i+1] * nums[i+1]
	}
	for i := 0; i < n; i++ {
		nums[i] = left[i] * right[i]
	}
	return nums
}
what is the intuition behind this solution?
The intuition behind this solution is to calculate the product of all elements to the left of the current element and the product of all elements to the right of the current element. We can then multiply these two products to get the product of all elements except the current element.

how did you arrive at this solution?
I arrived at this solution by observing that we can calculate the product of all elements to the left of the current element by keeping a running product of all elements to the left. Similarly, we can calculate the product of all elements to the right of the current element by keeping a running product of all elements to the right. We can then multiply these two products to get the desired result.

what are the key points of this solution?
The key points of this solution are:
- We use two arrays, left and right, to store the product of all elements to the left and right of the current element, respectively.
- We initialize the left array with 1 and calculate the product of all elements to the left of the current element by keeping a running product of all elements to the left.
- We initialize the right array with 1 and calculate the product of all elements to the right of the current element by keeping a running product of all elements to the right.
- We then multiply the corresponding elements of the left and right arrays to get the product of all elements except the current element.

what is the time and space complexity of this solution?
The time complexity of this solution is O(n), where n is the number of elements in the input array. The space complexity of this solution is O(n), as we use two additional arrays of size n to store the product of all elements to the left and right of the current element.