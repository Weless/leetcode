package main

import (
	"fmt"
	"sort"
)

func main() {
	nums := []int{8,1,2,2,3}
	fmt.Println(smallerNumbersThanCurrent(nums))
}

func smallerNumbersThanCurrent(nums []int) []int {

	temp := Temp{value:make([]int,len(nums))}
	copy(temp.value,nums)

	sort.Ints(nums)

	var result []int
	for _,i := range temp.value{
		for id,j := range nums {
			if i == j {
				result = append(result, id)
				break
			}
		}

	}
	return result
}

type Temp struct {
	value []int
}