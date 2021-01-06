package main

func maximumWealth(accounts [][]int) int {
	var max int
	for _, v := range accounts {
		sum := getSum(v)
		if sum > max {
			max = sum
		}
	}
	return max
}

func getSum(nums []int) int {
	var sum int
	for _, v := range nums {
		sum += v
	}
	return sum
}
