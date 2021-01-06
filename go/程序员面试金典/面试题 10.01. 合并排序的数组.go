package main

func merge(A []int, m int, B []int, n int) {
	i, j, k := m-1, n-1, len(A)-1
	for i >= 0 && j >= 0 {
		if B[j] >= A[i] {
			A[k] = B[j]
			j--
		} else {
			A[k] = A[i]
			i--
		}
		k--
	}
	for i >= 0 {
		A[k] = A[i]
		i--
		k--
	}

	for j >= 0 {
		A[k] = B[j]
		j--
		k--
	}
}
