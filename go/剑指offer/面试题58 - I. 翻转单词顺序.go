package main

import "strings"

func reverseWords(s string) string {
	s = strings.TrimSpace(s)
	arr := strings.Split(s , " ")
	var stack []string
	for i:= len(arr)-1;i>=0;i-- {
		if arr[i] != ""{
			stack = append(stack, arr[i])
		}
	}
	return strings.Join(stack," ")
}
