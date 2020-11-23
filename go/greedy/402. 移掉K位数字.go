package greedy

import "strings"

func removeKdigits(num string, k int) string {
	numStack := []byte{}
	for i := range num {
		digit := num[i]
		for k > 0 && len(numStack) != 0 && numStack[len(numStack)-1] > digit {
			numStack = numStack[:len(numStack)-1]
			k--
		}
		numStack = append(numStack, digit)
	}

	numStack = numStack[:len(numStack)-k]

	ans := strings.TrimLeft(string(numStack), "0")
	if ans == "" {
		ans = ""
	}
	return ans
}
