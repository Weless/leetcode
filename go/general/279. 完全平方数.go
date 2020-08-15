package main

import "math"

func numSquares(n int) int {
	squre_num := make([]int, 0)
	for i := 1; i < int(math.Sqrt(float64(n)))+1; i++ {
		squre_num = append(squre_num, i*i)
	}
	dp := make([]int, n+1)
	dp[0] = 0

	for i := 1; i < n+1; i++ {
		dp[i] = n + 1
	}
	for i := 1; i < n+1; i++ {
		for _, squre := range squre_num {
			if i < squre {
				break
			}
			dp[i] = min(dp[i], dp[i-squre]+1)
		}
	}
	return dp[n]
}

func min(a, b int) int {
	if a > b {
		return b
	} else {
		return a
	}

}
