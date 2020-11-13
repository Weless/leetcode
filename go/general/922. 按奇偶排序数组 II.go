package main

func sortArrayByParityII(A []int) []int {
	for i, j := 0, len(A)-1; i < len(A); i++ {
		if A[i]%2 != 0 {
			for j > 0 && A[j]%2 != 0 {
				j -= 2
			}
			A[i], A[j] = A[j], A[i]
		}
		i += 2
	}
	return A
}
