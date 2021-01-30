package array

func countElements(arr []int) int {
	d := make(map[int]struct{})
	ans := 0
	for _, v := range arr {
		if _, ok := d[v+1]; ok {
			ans++
		} else {
			if inArr(v+1, arr) {
				ans++
				d[v+1] = struct{}{}
			}
		}
	}
	return ans
}

func inArr(a int, A []int) bool {
	for _, v := range A {
		if v == a {
			return true
		}
	}
	return false
}
