package main

func minOperations(logs []string) int {
	var n int
	for _, v := range logs {
		if v == "./" {
			continue
		} else if v == "../" {
			if n == 0 {
				continue
			} else {
				n--
			}
		} else {
			n++
		}
	}
	return n
}
