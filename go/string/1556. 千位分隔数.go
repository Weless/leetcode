package string

import (
	"sort"
	"strconv"
	"strings"
)

func thousandSeparator(n int) string {
	if n < 1000 {
		return strconv.Itoa(n)
	}
	var res []string
	count := 0
	for n != 0 {
		a := n % 10
		n = n / 10
		res = append(res, strconv.Itoa(a))
		count++
		if count == 3 && n > 0 {
			res = append(res, ".")
			count = 0
		}
	}
	_ = sort.Reverse(sort.StringSlice(res))
	return strings.Join(res, "")
}
