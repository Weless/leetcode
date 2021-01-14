package array

func decode(encoded []int, first int) []int {
	before := first
	var res []int
	res = append(res, first)
	for i := 0; i < len(encoded); i++ {
		t := before ^ encoded[i]
		res = append(res, t)
		before = t
	}
	return res
}
