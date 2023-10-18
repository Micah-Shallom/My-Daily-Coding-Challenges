package challenges

import "fmt"

func rdSolution(arr []int) int {
	n := len(arr)
	if n == 0 {
		return 0
	}
	j := 0
	for i := 1; i < n; i++ {
		if arr[i] != arr[j] {
			j++
			arr[j] = arr[i]
		}
	}
	return j + 1
}

func RemoveDuplicates() {
	arr := []int{0,0,1,1,1,2,2,3,3,4}
	ans := rdSolution(arr)
	fmt.Println(ans)
}