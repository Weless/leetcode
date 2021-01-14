package array

func thirdMax(nums []int) int {
	var MIN = -1 << 63
	a, b, c := MIN, MIN, MIN

	for _, n := range nums {
		if n == a || n == b || n == c {
			continue
		}

		if n > a {
			a, b, c = n, a, b
		} else if n > b {
			b, c = n, b
		} else if n > c {
			c = n
		}
	}

	if c == MIN {
		return a
	}
	return c
}
