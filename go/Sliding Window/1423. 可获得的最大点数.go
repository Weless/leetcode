package window

func maxScore(cardPoints []int, k int) int {
	n := len(cardPoints) - k
	var sum int
	sum = getSum(cardPoints[:n])
	minNum := sum
	for i := n; i < len(cardPoints); i++ {
		sum += cardPoints[i] - cardPoints[i-n]
		if sum < minNum {
			minNum = sum
		}
	}
	return getSum(cardPoints) - minNum
}

func getSum(a []int) int {
	sum := 0
	for _, v := range a {
		sum += v
	}
	return sum
}
