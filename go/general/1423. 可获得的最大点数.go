package main

func sum(a []int) int {
	res := 0
	for _, i := range a {
		res += i
	}
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}

}

func maxScore(cardPoints []int, k int) int {
	res := sum(cardPoints)
	cur := res
	for i, _ := range cardPoints {
		cur += cardPoints[len(cardPoints)-1-i] - cardPoints[k-1-i]
		res = max(cur, res)
	}
	return res
}
