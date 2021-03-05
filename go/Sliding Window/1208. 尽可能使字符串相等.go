package window

func equalSubstring(s string, t string, maxCost int) int {
	left, right, totalCos := 0, 0, 0
	for right < len(s) {
		totalCos += abs(int(s[right] - t[right]))
		if totalCos > maxCost {
			totalCos -= abs(int(s[left] - t[left]))
			left++
		}
		right++
	}
	return right - left
}

func abs(a int) int {
	if a >= 0 {
		return a
	} else {
		return -1 * a
	}
}
