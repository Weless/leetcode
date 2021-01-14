package array

import (
	"fmt"
	"strconv"
)

func summaryRanges(nums []int) []string {
	var res []string
	for i := 0; i < len(nums); i++ {
		start := nums[i]
		for i < len(nums)-1 && nums[i+1]-nums[i] == 1 {
			i++
		}
		end := nums[i]
		if start == end {
			res = append(res, strconv.Itoa(start))
		} else {
			res = append(res, fmt.Sprintf("%d->%d", start, end))
		}
	}
	return res
}
