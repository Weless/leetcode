package stack

import "strconv"

func calPoints(ops []string) int {
	var res []int
	for _, v := range ops {
		if v == "C" {
			res = res[:len(res)-1]
		} else if v == "D" {
			res = append(res, res[len(res)-1]*2)
		} else if v == "+" {
			res = append(res, res[len(res)-1]+res[len(res)-2])
		} else {
			int_v, _ := strconv.Atoi(v)
			res = append(res, int_v)
		}
	}
	var sum int
	for _, v := range res {
		sum += v
	}
	return sum
}
