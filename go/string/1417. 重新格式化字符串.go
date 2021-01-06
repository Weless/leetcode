package string

import "fmt"

func reformat(s string) string {
	digit := []byte{}
	alpha := []byte{}
	for i := 0; i < len(s); i++ {
		if s[i] >= '0' && s[i] <= '9' {
			digit = append(digit, s[i])
		} else {
			alpha = append(alpha, s[i])
		}
	}
	fmt.Println(digit, alpha)
	l1, l2 := len(digit), len(alpha)
	if l1-l2 > 1 || l2-l1 > 1 {
		return ""
	}
	var res []byte
	if l1 >= l2 {
		for len(digit) != 0 {
			num := digit[len(digit)-1]
			digit = digit[:len(digit)-1]
			res = append(res, num)
			if len(alpha) != 0 {
				num = alpha[len(alpha)-1]
				alpha = alpha[:len(alpha)-1]
				res = append(res, num)
			}
		}
	} else {
		for len(alpha) != 0 {
			num := alpha[len(alpha)-1]
			alpha = alpha[:len(alpha)-1]
			res = append(res, num)
			if len(digit) != 0 {
				num = digit[len(digit)-1]
				digit = digit[:len(digit)-1]
				res = append(res, num)
			}
		}
	}
	fmt.Println(res)
	return string(res)
}
