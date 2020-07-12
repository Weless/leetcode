package main

func findContinuousSequence(target int) [][]int {
	i, j := 1, 1
	var res [][]int
	sum := 0
	for i < target/2 {
		if sum < target {
			sum += j
			j += 1
		} else if sum > target {
			sum -= i
			i += 1
		} else {
			var tmp []int
			for z := i; z < j; z++ {
				tmp = append(tmp, z)
			}
			res = append(res, tmp)
			sum -= i
			i += 1
		}
	}
	return res
}
