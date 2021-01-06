package main

func stringShift(s string, shift [][]int) string {
	for _, t := range shift {
		direction, amount := t[0], t[1]
		if amount == 0 {
			continue
		}
		if direction == 0 {
			s = s[amount:] + s[:amount]
		} else {
			s = s[len(s)-amount:] + s[:len(s)-amount]
		}
	}
	return s
}
