// Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

// Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 

// Example 1:

// Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
// Output: [2,2,2,1,4,3,3,9,6,7,19]
// Example 2:

// Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
// Output: [22,28,8,6,17,44]

package challenges

import (
	"sort"
)

func relativeSortArray(arr1 []int, arr2 []int) (res []int) {
    remainder_arr := []int{}
    arr1_hm := make(map[int]int)

    //create freequency based hashmap for arr1
    for _, v := range arr1 {
        arr1_hm[v]++
    }
    
    //loop through arr2 from left to right in its order and generate resulting arr based of it
    for _, x := range arr2 {
        val := arr1_hm[x]

        for val > 0 {
            res = append(res, x)
            val--
        }
        delete(arr1_hm, x)  
    }

    if len(arr1_hm) != 0 {
        for k, v := range arr1_hm {
            for v > 0 {
                remainder_arr = append(remainder_arr, k)
                v--
            }
        }
    }

    sort.Slice(remainder_arr, func(i, j int)bool {
        return remainder_arr[i] <= remainder_arr[j]
    })

    res = append(res, remainder_arr...)

    return res
}