package math

func isUgly(num int) bool {
	if num <= 0 {
		return false
	}
	tmp := []int{2, 3, 5}
	for _, v := range tmp {
		for num%v == 0 {
			num /= v
		}
	}
	if num == 1 {
		return true
	}
	return false
}
