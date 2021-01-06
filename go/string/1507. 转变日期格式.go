package string

import "strings"

func reformatDate(date string) string {
	monthMap := map[string]string{
		"Jan": "01",
		"Feb": "02",
		"Mar": "03",
		"Apr": "04",
		"May": "05",
		"Jun": "06",
		"Jul": "07",
		"Aug": "08",
		"Sep": "09",
		"Oct": "10",
		"Nov": "11",
		"Dec": "12",
	}
	dateString := strings.Split(date, " ")
	d := dateString[0]
	m := dateString[1]
	y := dateString[2]
	d = d[:len(d)-2]
	if len(d) == 1 {
		d = "0" + d
	}
	m = monthMap[m]
	return y + "-" + m + "-" + d
}
