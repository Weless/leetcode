package main

import "strings"

func uncommonFromSentences(A string, B string) []string {
	d1, d2 := make(map[string]int), make(map[string]int)

	tmpA := strings.Split(A, " ")
	tmpB := strings.Split(B, " ")

	for _, v := range tmpA {
		d1[v]++
	}

	for _, v := range tmpB {
		d2[v]++
	}

	var res []string

	for k, v := range d1 {
		if v == 1 {
			if _, ok := d2[k]; !ok {
				res = append(res, k)
			}
		}
	}

	for k, v := range d2 {
		if v == 1 {
			if _, ok := d1[k]; !ok {
				res = append(res, k)
			}
		}
	}

	return res 
}
