package string

func calculateTime(keyboard string, word string) int {
	var index = make(map[byte]int)
	for i := 0; i < len(keyboard); i++ {
		index[keyboard[i]] = i
	}
	tmp := string(keyboard[0]) + word

	ans := 0
	pre := 0
	for i := 1; i < len(tmp); i++ {
		t := index[tmp[i]] - pre
		if t < 0 {
			t = -t
		}
		ans += t
		pre = index[tmp[i]]
	}
	return ans
}
