package math

func totalMoney(n int) int {
	week := 0
	res := 0
	for n != 0 {
		if n >= 7 {
			res += week*7 + (1 + 2 + 3 + 4 + 5 + 6 + 7)
			n -= 7
		} else {
			res += week * n
			for n != 0 {
				res += n
				n--
			}
		}
		week++
	}
	return res
}
