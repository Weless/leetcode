package window

func longestOnes(A []int, K int) int {
	left, right := 0, 0
	for ; right < len(A); right++ {
		if A[right] == 0 {
			K--
		}
		if K < 0 {
			if A[left] == 0 {
				K++
			}
			left++
		}
	}
	return right - left
}
