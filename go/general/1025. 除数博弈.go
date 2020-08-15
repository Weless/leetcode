package main

func divisorGame(N int) bool {
	if N == 1 {
		return false
	}
	dp := make([]bool, N+1)
	dp[1] = false
	dp[2] = true

	for i := 3; i < N+1; i++ {
		dp[i] = false
		for x := 1; x < i; x++ {
			if i%x == 0 && dp[i-x] == false {
				dp[i] = true
				break
			}
		}
	}
	return dp[N]
}
