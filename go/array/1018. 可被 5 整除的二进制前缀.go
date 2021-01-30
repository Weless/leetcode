package array

func prefixesDivBy5(A []int) []bool {
	var res []bool
	tmp := 0
	for _, v := range A {
		tmp = (tmp*2 + v) % 5
		res = append(res, tmp == 0)
	}
	return res
}
