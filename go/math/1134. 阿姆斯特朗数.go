package math

import "math"

func isArmstrong(N int) bool {
	ans := 0
	var res []int
	M := N
	for M != 0 {
		res = append(res, M%10)
		M /= 10
	}
	for _, v := range res {
		ans += int(math.Pow(float64(v), float64(len(res))))
	}
	return ans == N
}
