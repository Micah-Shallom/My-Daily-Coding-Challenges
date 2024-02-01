package challenges

import "fmt"

func ngeSolution(nums1, nums2 []int) []int {
	arr := []int{}
	for i:= 0 ; i < len(nums1); i++ {
		idx := -1

		for j:= 0; j < len(nums2); j ++ {
			if nums1[i] == nums2[j] {
				idx = j
			}
		}

		if idx != -1 { 
			found := false
			for k:=idx; k < len(nums2); k++ {
				if nums2[k] > nums2[idx]{
					found = true
					arr = append(arr, nums2[k])
					break
				}
			}

			if !found {
				arr = append(arr, -1)
			}
		}
		
	}
	return arr
}

func NextGreaterElement() {
	nums1 := []int{4, 1, 2}
	nums2 := []int{1, 3, 4, 2}
	a := ngeSolution(nums1, nums2)
	fmt.Println(a)
}
