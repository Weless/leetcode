package string

func validPalindrome(s string) bool {
	var isValidPalindrome func(int, int) bool
	isValidPalindrome = func(low, high int) bool {
		i, j := low, high
		for i < j {
			if s[i] == s[j] {
				i++
				j--
			} else {
				return false
			}
		}
		return true
	}

	i, j := 0, len(s)-1
	for i < j {
		if s[i] == s[j] {
			i++
			j--
		} else {
			return isValidPalindrome(i+1, j) || isValidPalindrome(i, j-1)
		}
	}
	return true
}
