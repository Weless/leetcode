package main

import (
	"fmt"
	"sort"
)

func intersection2(nums1 []int, nums2 []int) []int {
	sort.Ints(nums1)
	sort.Ints(nums2)
	ret := []int{}
	i, j := 0, 0
	for i < len(nums1) && j < len(nums2) {
		if nums1[i] == nums2[j] {
			if len(ret) == 0 || ret[len(ret)-1] != nums1[i] {
				ret = append(ret, nums1[i])
			}
			i++
			j++
		} else if nums1[i] < nums2[j] {
			i++
		} else {
			j++
		}
	}
	return ret
}

func main() {
	nums1, nums2 := []int{4, 9, 5}, []int{9, 4, 9, 8, 4}
	fmt.Println(intersection2(nums1, nums2))
}
