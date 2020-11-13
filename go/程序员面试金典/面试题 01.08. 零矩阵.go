package main

func setZeroes(matrix [][]int) {
	m, n := len(matrix), len(matrix[0])
	isRowZero, isColZero := false, false
	for i := 0; i < m; i++ {
		if matrix[i][0] == 0 {
			isColZero = true
		}
	}

	for i := 0; i < n; i++ {
		if matrix[0][i] == 0 {
			isRowZero = true
		}
	}

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if matrix[i][j] == 0 {
				matrix[i][0] = 0
				matrix[0][j] = 0
			}
		}
	}

	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if matrix[i][0] == 0 || matrix[0][j] == 0 {
				matrix[i][j] = 0
			}
		}
	}

	for i := 0; i < m; i++ {
		if isColZero {
			matrix[i][0] = 0
		}
	}

	for i := 0; i < n; i++ {
		if isRowZero {
			matrix[0][i] = 0
		}
	}
}
