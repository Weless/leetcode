package main

func maxProfit(prices []int) int {
	if len(prices) == 0 {
		return 0
	}
	cost := prices[0]
	max := 0
	for i := 1; i < len(prices); i++ {
		if prices[i] < cost {
			cost = prices[i]
		}
		if prices[i]-cost > max {
			max = prices[i] - cost
		}
	}
	return max
}
