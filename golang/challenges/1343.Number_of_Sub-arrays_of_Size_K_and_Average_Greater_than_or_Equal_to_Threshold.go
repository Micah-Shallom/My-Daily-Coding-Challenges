package challenges

import "fmt"

// # Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

// # Example 1:

// # Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
// # Output: 3
// # Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
// # Example 2:

// # Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
// # Output: 6
// # Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
 
func nsaSolution(arr []int, k int, threshold int) int{
	count := 0
	currSum := sum(arr[:k-1])

	for i := 0; i < len(arr) - k + 1 ; i ++ {
		currSum += arr[i + k -1]

		if (currSum/k) >= threshold{
			count += 1
		}
		currSum -= 1
	}
	return count
}

func NumSubArray(){
	arr := []int{2,2,2,2,5,5,5,8}
	k := 3
	threshold := 4
	fmt.Println(nsaSolution(arr,k,threshold))
}