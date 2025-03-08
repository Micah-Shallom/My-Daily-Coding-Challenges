// 2570. Merge Two 2D Arrays by Summing Values
// Solved
// Easy
// Topics
// Companies
// Hint
// You are given two 2D integer arrays nums1 and nums2.

// nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
// nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
// Each array contains unique ids and is sorted in ascending order by id.

// Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

// Only ids that appear in at least one of the two arrays should be included in the resulting array.
// Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
// Return the resulting array. The returned array must be sorted in ascending order by id.

 

// Example 1:

// Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
// Output: [[1,6],[2,3],[3,2],[4,6]]
// Explanation: The resulting array contains the following:
// - id = 1, the value of this id is 2 + 4 = 6.
// - id = 2, the value of this id is 3.
// - id = 3, the value of this id is 2.
// - id = 4, the value of this id is 5 + 1 = 6.
// Example 2:

// Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
// Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
// Explanation: There are no common ids, so we just include each id with its value in the resulting list.

func mergeArrays(nums1 [][]int, nums2 [][]int) (res [][]int) {
    p1, p2 := 0, 0

    for p1 < len(nums1) && p2 < len(nums2){
        v1,v2 := nums1[p1], nums2[p2]

        if v1[0] < v2[0]{
            res = append(res, v1)
            p1++
        }else if v1[0] > v2[0]{
            res = append(res, v2)
            p2++
        }else{
            res = append(res, []int{v1[0], v1[1]+v2[1]})
            p1++
            p2++
        }
    }

    for p1 < len(nums1) {
        res = append(res, nums1[p1])
        p1++
    }
    for p2 < len(nums2) {
        res = append(res, nums2[p2])
        p2++
    }

    return 
}
