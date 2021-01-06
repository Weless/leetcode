package main

func numberOfDays(Y int, M int) int {
	switch M {
	case 1, 3, 5, 7, 8, 10, 12:
		return 31
	case 4, 6, 9, 11:
		return 30
	default:
		if checkLeapYear(Y) {
			return 29
		} else {
			return 28
		}
	}
}

func checkLeapYear(year int) bool {
	if year%400 == 0 {
		return true
	}
	if year%4 == 0 && year%100 != 0 {
		return true
	}
	return false
}
