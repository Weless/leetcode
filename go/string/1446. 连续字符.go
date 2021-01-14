package string

func maxPower(s string) int {
	res := 1
	for i := 1; i < len(s); i++ {
		tmp := 1
		for s[i] == s[i-1] {
			tmp++
			i++
		}
		if tmp > res {
			res = tmp
		}
	}
	return res
}
