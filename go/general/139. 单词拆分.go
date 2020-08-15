package main

func wordBreak(s string, wordDict []string) bool {
	n := len(s)
	dp := make([]bool, n+1)
	dp[0] = true
	for i := 1; i < n+1; i++ {
		dp[i] = false
	}
	for i := 0; i < n+1; i++ {
		for j := i + 1; j < n+1; j++ {
			if dp[i] && inString(s[i:j], wordDict) {
				dp[j] = true
			}
		}
	}
	return dp[n]
}

func inString(s string, t []string) bool {
	for _, v := range t {
		if s == v {
			return true
		}
	}
	return false
}
