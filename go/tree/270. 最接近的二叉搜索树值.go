package tree

func closestValue(root *TreeNode, target float64) int {
	ret := root.Val
	bl := abs(float64(root.Val), target)
	a := 0.0
	for root != nil {
		a = abs(float64(root.Val), target)
		if a < bl {
			ret = root.Val
			bl = a
		}
		if target > float64(root.Val) {
			root = root.Right
		} else {
			root = root.Left
		}
	}
	return ret
}

func abs(a, b float64) float64 {
	if a > b {
		return a - b
	} else {
		return b - a
	}
}
