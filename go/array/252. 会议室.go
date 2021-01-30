package array

import (
	"sort"
)

func canAttendMeetings(intervals [][]int) bool {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	i := 1
	for i < len(intervals) {
		if intervals[i][0] < intervals[i-1][1] {
			return false
		}
		i++
	}
	return true
}
