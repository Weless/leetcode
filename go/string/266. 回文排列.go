package string

func canPermutePalindrome(s string) bool {
	d := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		d[s[i]]++
	}
	l := len(s)
	if l%2 == 0 {
		for _, v := range d {
			if v%2 != 0 {
				return false
			}
		}
		return true
	} else {
		count := 0
		for _, v := range d {
			if v%2 != 0 {
				count++
			}
			if count > 1 {
				return false
			}
		}
		return true
	}
}
