package main

func fixedPoint(A []int) int {
	for i, v := range A {
		if i == v {
			return i
		}
	}
	return -1
}
