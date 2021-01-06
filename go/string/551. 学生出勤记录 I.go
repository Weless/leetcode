package string

func checkRecord(s string) bool {
	d := make(map[rune]int)
	c := 0
	for _, v := range s {
		switch v {
		case 'A':
			d['A']++
			c = 0
		case 'L':
			c++
			if c > 2 {
				return false
			}
			d['L']++
		case 'P':
			d['P']++
			c = 0
		}
	}
	if v, ok := d['A']; ok {
		if v > 1 {
			return false
		}
	}
	return true
}
