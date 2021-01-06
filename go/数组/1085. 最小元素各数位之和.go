package main

import "math"

func sumOfDigits(A []int) int {
	var ans int
	minNum := math.MaxInt32
	for _, v := range A {
		if v < minNum {
			minNum = v
		}
	}
	for minNum != 0 {
		ans += minNum % 10
		minNum /= 10
	}
	if ans%2 == 0 {
		return 1
	} else {
		return 0
	}
}
