package array

import (
	"sort"
)

func arrayRankTransform(arr []int) []int {
	d := make(map[int]int)
	var tmp []int
	copy(tmp, arr)
	sort.Ints(tmp)
	i := 1
	for _, v := range tmp {
		if d[v] == 0 {
			d[v] = i
			i++
		}
	}
	var res []int
	for _, v := range arr {
		res = append(res, d[v])
	}
	return res
}
