package array

func numEquivDominoPairs(dominoes [][]int) int {
	nums := make([]int, 100)
	var res int
	for i, _ := range dominoes {
		x, y := dominoes[i][0], dominoes[i][1]
		var val int
		if x < y {
			val = x*10 + y
		} else {
			val = y*10 + x
		}
		res += nums[val]
		nums[val]++
	}
	return res
}
