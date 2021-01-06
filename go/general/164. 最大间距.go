package main

import "sort"

func maximumGap(nums []int) int {
	if len(nums) == 0 || len(nums) == 1 {
		return 0
	}
	sort.Ints(nums)
	res := -1
	for i := 0; i < len(nums)-1; i++ {
		j := i + 1
		if nums[j]-nums[i] >= 0 {
			if res < nums[j]-nums[i] {
				res = nums[j] - nums[i]
			}
		} else {
			if res < nums[i]-nums[j] {
				res = nums[i] - nums[j]
			}
		}
	}
	return res
}
