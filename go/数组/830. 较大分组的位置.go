package main

func largeGroupPositions(s string) [][]int {
	var res [][]int
	for i := 0; i < len(s)-1; {
		j := i + 1
		for j < len(s) {
			if s[j] != s[i] {
				break
			}
			j += 1
		}
		if j-i >= 3 {
			res = append(res, []int{i, j - 1})
		}
		i = j
	}
	return res
}
