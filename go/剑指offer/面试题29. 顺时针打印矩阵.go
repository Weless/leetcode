package main

func spiralOrder(matrix [][]int) []int {
	var res []int
	if matrix == nil {
		return res
	}
	l, r, t, b := 0, len(matrix[0])-1, 0, len(matrix)-1
	for true {
		for i := l; i <= r; i++ {
			res = append(res, matrix[t][i])
		}
		t += 1
		if t > b {
			break
		}
		for i := t; i <= b; i++ {
			res = append(res, matrix[i][r])
		}
		r -= 1
		if l > r {
			break
		}
		for i := r; i >= l; i-- {
			res = append(res, matrix[b][i])
		}
		b -= 1
		if t > b {
			break
		}
		for i := b; i >= t; i-- {
			res = append(res, matrix[i][l])
		}
		l += 1
		if l > r {
			break
		}
	}
	return res
}
