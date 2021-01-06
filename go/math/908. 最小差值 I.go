package math

import "math"

func smallestRangeI(A []int, K int) int {
	max, min := getMax(A), getMin(A)
	if max-min <= 2*K {
		return 0
	} else {
		return max - min - 2*K
	}
}

func getMax(A []int) int {
	var max int
	max = math.MinInt32
	for _, v := range A {
		if v > max {
			max = v
		}
	}
	return max
}

func getMin(A []int) int {
	var min int
	min = math.MaxInt32
	for _, v := range A {
		if v < min {
			min = v
		}
	}
	return min
}
