package game

func tupleSameProduct(nums []int) int {
	d := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			d[nums[i]*nums[j]]++
		}
	}

	var res int
	for _, v := range d {
		res += v * (v - 1) / 2
	}
	return res * 8
}
