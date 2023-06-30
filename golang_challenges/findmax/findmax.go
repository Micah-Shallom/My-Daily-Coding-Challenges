package findmax


func FindMaxArray(arr []int) int {
	maxArr := arr[0]

	if len(arr) == 0 {
		return -1
	}

	for _, v := range arr {
		if v > maxArr {
			maxArr = v
		}
	}

	return maxArr
}