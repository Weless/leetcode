package array

import "math"

func largestAltitude(gain []int) int {
	res := make([]int, len(gain)+1)
	for i := 0; i < len(gain); i++ {
		res[i+1] = res[i] + gain[i]
	}
	max := math.MinInt32
	for _, v := range res {
		if v > max {
			max = v
		}
	}
	return max
}
