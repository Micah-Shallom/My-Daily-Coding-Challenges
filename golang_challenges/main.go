package main

import (
	"modules.com/micah/golang_challenges/findmax"
	"fmt"
)

func findmaxfunc(){
	p := fmt.Println
	arr := []int{3, 6, 3, 5, 9}
	p(findmax.FindMaxArray(arr))
}





func main() {
	findmaxfunc()
}