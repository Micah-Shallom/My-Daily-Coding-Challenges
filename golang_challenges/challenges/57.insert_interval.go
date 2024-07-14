// You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

// Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

// Return intervals after the insertion.

// Note that you don't need to modify intervals in-place. You can make a new array and return it.

// Example 1:

// Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
// Output: [[1,5],[6,9]]
// Example 2:

// Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
// Output: [[1,2],[3,10],[12,16]]
// Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
package challenges

import "fmt"

func someFunction(intervals [][]int, newinterval []int) [][]int {
	new_arr := [][]int{}
	i := 0
	
	for i < len(intervals) && intervals[i][1] < newinterval[0]{
		new_arr = append(new_arr, intervals[i])
		i++
	}

	for i < len(intervals) && (intervals[i][0] <= newinterval[1]){
		newinterval[0] = min(intervals[i][0], newinterval[0])
		newinterval[1] = max(intervals[i][1], newinterval[1])
		i++
	}
	new_arr = append(new_arr, newinterval)

	for i < len(intervals){
		new_arr = append(new_arr, intervals[i])
		i++
	}

	return new_arr
}


func Insert() {
	intervals := [][]int{{1, 2}, {5, 6}, {6, 7}, {8, 10}, {12, 16}}
	newInterval := []int{4, 8}

	fmt.Println(someFunction(intervals, newInterval))
}