package window

func maxSatisfied(customers []int, grumpy []int, X int) int {
	left, right := 0, X
	n := 0
	for _, v := range customers[left:right] {
		n += v
	}
	i := right
	for i < len(customers) {
		if grumpy[i] == 0 {
			n += customers[i]
		}
		i++
	}
	maxNum := n
	for right < len(customers) {
		if grumpy[right] == 1 {
			n += customers[right]
		}
		if grumpy[left] == 1 {
			n -= customers[left]
		}
		if n > maxNum {
			maxNum = n
		}
		right++
		left++
	}
	return maxNum
}
