package main

// 暴力，golang
func largestRectangleArea(heights []int) int {
	if len(heights) == 0 {
		return 0
	}
	if len(heights) == 1 {
		return heights[0]
	}
	i := 0
	max := -1
	for i < len(heights) {
		j := i + 1
		z := i - 1
		d1, d2 := 0, 0
		for j < len(heights) && heights[i] <= heights[j] {
			j++
			d1++
		}
		for z >= 0 && heights[i] <= heights[z] {
			z--
			d2++
		}
		t := heights[i] * (1 + d1 + d2)
		if max < t {
			max = t
		}
		i++
	}
	return max
}
