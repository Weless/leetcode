package array

import "sort"

func relativeSortArray(arr1 []int, arr2 []int) []int {
	var d = make(map[int]int)
	var tmp []int
	var res []int
	sort.Ints(arr1)
	for _, v := range arr1 {
		if _, ok := d[v]; !ok {
			d[v] = 1
		} else {
			d[v]++
		}
		if inSlice(v, arr2) == false {
			tmp = append(tmp, v)
		}
	}
	for _, v := range arr2 {
		for i := 0; i < d[v]; i++ {
			res = append(res, v)
		}
	}
	res = append(res, tmp...)
	return res
}

func inSlice(e int, slice []int) bool {
	for _, s := range slice {
		if s == e {
			return true
		}
	}
	return false
}
