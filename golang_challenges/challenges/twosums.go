package challenges

import "fmt"


func solution(arr []int, target int) []int {
	var hashmap = map[int]int{}

	for idx, val := range arr {
		diff := target - val
		if hval, found := hashmap[diff]; found {
			return []int{hval, idx}
		}
		hashmap[val] = idx
	}
	return []int{}
}

func Twosums() {
	s := solution([]int{2,7,4,5,6}, 9)
	fmt.Println(s)
}
