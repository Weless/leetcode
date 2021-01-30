package array

func numSmallerByFrequency(queries []string, words []string) []int {
	var f func(string) int
	f = func(s string) int {
		num := 0
		mStr := byte('z')
		for i := 0; i < len(s); i++ {
			if s[i] < mStr {
				mStr = s[i]
				num = 1
			} else {
				num++
			}
		}
		return num
	}

	var res []int
	for _, v1 := range queries {
		c := 0
		for _, v2 := range words {
			if f(v1) < f(v2) {
				c++
			}
		}
		res = append(res, c)
	}
	return res
}
