package main

import "fmt"

func majorityElement(nums []int) []int {
	cnt := len(nums) / 3

	cntMap := make(map[int]int)

	var res []int

	for _, v := range nums {
		cntMap[v]++
	}

	for k, v := range cntMap {
		if v > cnt {
			res = append(res, k)
		}
	}
	return res
}

func main() {
	nums := []int{1, 1, 1, 3, 3, 2, 2, 2}
	fmt.Println(majorityElement(nums))
}
