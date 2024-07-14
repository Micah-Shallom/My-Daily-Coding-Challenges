// Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

// Example 1:

// Input: nums1 = [1,2,2,1], nums2 = [2,2]
// Output: [2]
// Example 2:

// Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// Output: [9,4]
// Explanation: [4,9] is also accepted.
package challenges

import (
	"fmt"
	"sort"
)

func intSolution(nums1 []int, nums2 []int) (res []int) {
	hashMap := make(map[int]bool)
    sort.Ints(nums1)
    sort.Ints(nums2)

    for i, j := 0, 0; i < len(nums1) && j < len(nums2); {
        if nums1[i] < nums2[j]{
            i++
        }else if nums1[i] > nums2[j]{
            j++
        }else{
            if _, exists := hashMap[nums1[i]]; !exists{
                hashMap[nums1[i]] = true
                res = append(res, nums1[i])
            }
            i++
            j++
        }
    }
    return 
}

func intSolution1(nums1 []int, nums2 []int) []int {
	res := []int{}
    hashMap := map[int]int{}
    set := map[int]int{}

    for _, val := range nums1{
        hashMap[val]++
    }

    for _, val := range nums2{
        if _, found := hashMap[val]; found {
            set[val] = 0
        }
    }
    
    for key, _ := range set{
        res = append(res, key)
    }
    return res
}

func Intersection(){
	fmt.Println(intSolution([]int{1,2,2,1}, []int{2,2}))
}