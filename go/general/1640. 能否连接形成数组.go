package main

func canFormArray(arr []int, pieces [][]int) bool {
	d := make(map[int][]int)
	for _, v := range pieces {
		d[v[0]] = v
	}
	for i := 0; i < len(arr); {
		if _, ok := d[arr[i]]; !ok {
			return false
		}
		for _, v := range d[arr[i]] {
			if arr[i] != v {
				return false
			}
			i += 1
		}
	}
	return true
}
