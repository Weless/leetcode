package string

func firstUniqChar(s string) int {
	d := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		d[s[i]]++
	}
	for i := 0; i < len(s); i++ {
		if d[s[i]] == 1 {
			return i
		}
	}
	return -1
}
