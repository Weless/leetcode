package greedy

import "sort"

func findMinArrowShots(points [][]int) int {
	if len(points) == 0 {
		return 0
	}
	sort.Slice(points, func(i, j int) bool {
		x := points[i]
		y := points[j]
		return x[1] < y[1]
	})
	pos := points[0][1]
	ans := 1
	for _, v := range points {
		if v[0] > pos {
			pos = v[1]
			ans++
		}
	}
	return ans
}
