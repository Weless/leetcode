package string

func canConstruct(ransomNote string, magazine string) bool {
	d := make(map[rune]int)
	for _, v := range magazine {
		d[v]++
	}
	for _, v := range ransomNote {
		if _, ok := d[v]; ok {
			d[v]--
			if d[v] < 0 {
				return false
			}
		} else {
			return false
		}
	}
	return true
}
