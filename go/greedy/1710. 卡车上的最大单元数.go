package greedy

import (
	"fmt"
	"sort"
)

func maximumUnits(boxTypes [][]int, truckSize int) int {
	sort.Slice(boxTypes, func(i, j int) bool {
		return boxTypes[j][1] < boxTypes[i][1]
	})
	fmt.Println(boxTypes)
	var res int
	for _, v := range boxTypes {
		x, y := v[0], v[1]
		if truckSize >= x {
			res += x * y
			truckSize -= x
		} else {
			res += y * truckSize
			truckSize = 0
		}
		if truckSize == 0 {
			break
		}
	}
	return res
}
