package main

import "sort"

func allCellsDistOrder(R int, C int, r0 int, c0 int) [][]int {
	var res [][]int
	for i := 0; i < R; i++ {
		for j := 0; j < C; j++ {
			res = append(res, []int{i, j})
		}
	}
	sort.Slice(res, func(i, j int) bool {
		a, b := res[i], res[j]
		return abs(a[0]-r0)+abs(a[1]-c0) < abs(b[0]-r0)+abs(b[1]-c0)
	})
	return res
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
