package main

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func maxScore(s string) int {
	res := -1
	left := 0
	right := 0
	for i, v := range s {
		if v == '0' {
			left += 1
		} else {
			left -= 1
			right += 1
		}
		if i < len(s)-1 {
			res = max(left, res)
		}
	}
	return res + right
}
