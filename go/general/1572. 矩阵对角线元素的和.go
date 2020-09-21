package main

func diagonalSum(mat [][]int) int {
	l := len(mat)
	var res int
	for i := 0; i < l; i++ {
		res += mat[i][i]
		res += mat[i][l-1-i]
	}
	if l%2 == 0 {
		return res
	} else {
		return res - mat[l/2][l/2]
	}
}
