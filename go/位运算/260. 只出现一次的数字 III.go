package main

func singleNumber(nums []int) []int {
	mask := 0
	for _, v := range nums {
		mask ^= v
	}
	diff := mask & (-mask)

	res := 0
	for _, v := range nums {
		if diff&v != 0 {
			res ^= v
		}
	}
	return []int{res, res ^ mask}
}
