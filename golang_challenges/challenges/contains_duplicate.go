package challenges

import "fmt"

func duplicateSolution(nums []int) bool {
	hashmap := map[int]int{}
	for _ , num := range nums {
		if _ , found := hashmap[num]; found {
			return true
		}
		hashmap[num] = 0
	}
	return false
}

func Duplicate() {
	d := duplicateSolution([]int{1, 2, 3, 4})	
	fmt.Println(d)
}