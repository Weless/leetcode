package array

import (
	"sort"
)

func frequencySort(nums []int) []int {
	hash := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		hash[nums[i]]++
	}
	sort.Slice(nums, func(i, j int) bool {
		if hash[nums[i]] == hash[nums[j]] {
			return nums[i] > nums[j]
		}
		return hash[nums[i]] < hash[nums[j]]
	})
	return nums
}
