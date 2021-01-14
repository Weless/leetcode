package string

import (
	"strings"
)

func toGoatLatin(S string) string {
	res := strings.Split(S, " ")
	for i, v := range res {
		b := []byte(v)
		switch b[0] {
		case 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U':
			res[i] += "ma"
			res[i] += strings.Repeat("a", i+1)
		default:
			res[i] = res[i][1:] + res[i][0:1] + "ma"
			res[i] += strings.Repeat("a", i+1)
		}
	}
	return strings.Join(res, " ")
}
