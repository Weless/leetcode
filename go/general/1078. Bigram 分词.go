package main

import "strings"

func findOcurrences(text string, first string, second string) []string {
	var tmpText []string
	tmpText = strings.Split(text, " ")
	var res []string
	for i := 0; i < len(tmpText)-2; i++ {
		if tmpText[i] == first && tmpText[i+1] == second {
			res = append(res, tmpText[i+2])
		}
	}
	return res
}
