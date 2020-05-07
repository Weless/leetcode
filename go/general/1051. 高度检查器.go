package main

func heightChecker(heights []int) int {
	arr := make([]int, 101)

	for _, v := range heights {
		arr[v]++
	}
	count := 0
	for i, j := 1, 0; i < len(arr); i++ {
		for arr[i] > 0 {
			arr[i]--
			if heights[j] != i {
				count++
			}
			j++
		}
	}
	return count
}
