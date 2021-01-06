package math

func isStrobogrammatic(num string) bool {
	var items []int
	N, _ := strconv.Atoi(num)
	M := N
	for M != 0 {
		items = append(items, M%10)
		M /= 10
	}
	for _, v := range items {
		switch v {
		case 2, 3, 4, 5, 7:
			return false
		}
	}
	var res int
	for i := 0; i < len(items); i++ {
		res *= 10
		switch items[i] {
		case 0:
			res += 0
		case 1:
			res += 1
		case 6:
			res += 9
		case 9:
			res += 6
		case 8:
			res += 8
		}
	}
	return res == N
}
