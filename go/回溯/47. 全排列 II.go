package main

import (
	"fmt"
	"sort"
)

var res [][]int

func permuteUnique(nums []int) [][]int {
	var path []int
	sort.Ints(nums)
	dfs(path, nums)
	return res
}

func dfs(path []int, choice []int) {
	if len(path) == len(choice) {
		res = append(res, path)
		return
	}
	for i := 0; i < len(choice); i++ {
		if i > 0 && choice[i] == choice[i-1] {
			continue
		}
		path = append(path, choice[i])
		//tmp := append(choice[:i], choice[i+1:]...)
		dfs(path, choice)
		//path = path[:len(choice)-1]
	}
}

func main() {
	nums := []int{1, 2, 3}
	fmt.Println(permuteUnique(nums))
}
