package array

func specialArray(nums []int) int {
	for i := 1; i <= len(nums); i++ {
		count := 0
		for _, v := range nums {
			if v >= i {
				count++
			}
		}
		if count == i {
			return count
		}
	}
	return -1
}
