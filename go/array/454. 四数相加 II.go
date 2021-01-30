package array

func fourSumCount(A []int, B []int, C []int, D []int) int {
	var d = make(map[int]int)
	for _, v1 := range A {
		for _, v2 := range B {
			d[v1+v2]++
		}
	}
	var ans int
	for _, v1 := range C {
		for _, v2 := range D {
			if k, ok := d[-v1-v2]; ok {
				ans += k
			}
		}
	}
	return ans
}
