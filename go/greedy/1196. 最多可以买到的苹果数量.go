package greedy

import "sort"

func maxNumberOfApples(arr []int) int {
	sort.Ints(arr)
	n := 0
	ans := 5000
	for _, v := range arr {
		if v > ans {
			return n
		} else {
			ans -= v
			n++
		}
	}
	return n
}
