package algorithms

import "fmt"

// bubble sort algorithms
func bsSolution(customlist []int) []int {
	for i := 0; i < len(customlist)-1; i++ {
		for j := 0; j < len(customlist)-i-1; j++ {
			if customlist[j] > customlist[j+1] {
				customlist[j], customlist[j+1] = customlist[j+1], customlist[j]
			}
		}
	}
	return customlist
}

//selection sorting algorithm
func ssSolution(customlist []int) []int{
	for i := 0; i < len(customlist); i++ {
		min_index := i

		for j := i; j < len(customlist); j ++ {
			if customlist[min_index] > customlist[j]{
				min_index = j
			}
		}
		customlist[min_index], customlist[i] = customlist[i], customlist[min_index]
	}
	return customlist
}


func SimpleSortingAlgorithms() {
	clist := []int{1, 6, 9, 4, 7, 6, 3, 3, 6, 5, 5, 7, 5, 7, 5, 3, 2, 3, 8, 9, 7, 4, 9, 5, 3}
	fmt.Println("Bubble Sort ->",bsSolution(clist))
	fmt.Println("Selection Sort ->",ssSolution(clist))
}