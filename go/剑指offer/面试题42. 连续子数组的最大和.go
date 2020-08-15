package main

func maxSubArray(nums []int) int {
	if nums == nil {
		return 0
	}
	n := len(nums)
	dp := make([]int, n)
	dp[0] = nums[0]
	for i := 1; i < n; i++ {
		if dp[i-1] > 0 {
			dp[i] = dp[i-1] + nums[i]
		} else {
			dp[i] = nums[i]
		}
	}
	return max(dp)
}

func max(t []int) int {
	tmp := -1000000
	for _, v := range t {
		if v > tmp {
			tmp = v
		}
	}
	return tmp
}
