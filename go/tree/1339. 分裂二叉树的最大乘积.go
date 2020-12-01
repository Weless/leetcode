package tree

import "math"

var res map[int]struct{}

func maxProduct(root *TreeNode) int {
	res = make(map[int]struct{})
	num := getSum(root)
	ans := 0
	for k, _ := range res {
		if ans > k*(num-k) {
			continue
		} else {
			ans = k * (num - k)
		}
	}
	return ans % (int(math.Pow(10, 9)) + 7)
}

func getSum(root *TreeNode) int {
	if root == nil {
		return 0
	}
	val := root.Val + getSum(root.Left) + getSum(root.Right)
	res[val] = struct{}{}
	return val
}
