package challenges

import "fmt"

func rdSolution(arr []int) int {
	j := 1 
	for i := 1; i < len(arr); i++ {
		if arr[i] != arr[i-1]{
			arr[j] = arr[i]
			j += 1
		}
	}
	return j
}

func RemoveDuplicates() {
	arr := []int{0,0,1,1,1,2,2,3,3,4}
	ans := rdSolution(arr)
	fmt.Println(ans)
}