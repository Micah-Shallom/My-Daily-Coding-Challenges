package challenges

import (
	"fmt"
	"math"
)

// # Given an array nums of size n, return the majority element.

// # The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

// # Example 1:

// # Input: nums = [3,2,3]
// # Output: 3
// # Example 2:

// # Input: nums = [2,2,1,1,1,2,2]
// # Output: 2

func solutionMajorityElements(arr []int) int {
	hashmap := make(map[int]int)
	bench := int(math.Floor(float64(len(arr)) / 2))
	fmt.Println(bench)
	for _, val := range arr {
		_, found := hashmap[val]
		if found {
			hashmap[val] += 1
		} else {
			hashmap[val] = 1
		}
	}
	fmt.Println(hashmap)
	for key, val := range hashmap {
		if val >= bench {
			return key
		}
	}
	return 0
}

func MajorityElements() {
	arr := []int{3,2,3}
	fmt.Println(solutionMajorityElements(arr))
}
