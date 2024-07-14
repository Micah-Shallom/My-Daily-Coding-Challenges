// Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

// Example 1:

// Input: arr = [2,6,4,1]
// Output: false
// Explanation: There are no three consecutive odds.
// Example 2:

// Input: arr = [1,2,34,3,4,5,7,23,12]
// Output: true
// Explanation: [5,7,23] are three consecutive odds.

package challenges

func threeConsecutiveOdds(arr []int) bool {
    count := 0
    
    for _ , v := range arr {
        if count <= 0{
            count = 0
        }
        if v % 2 != 0 {
            count++
        }else{
            count = 0
        }
        if count == 3{
            return true
        }
    }
    return false
}