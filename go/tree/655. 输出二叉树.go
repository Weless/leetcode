package tree

import (
	"math"
	"strconv"
)

func printTree(root *TreeNode) [][]string {
	var dfs func(*TreeNode) int
	dfs = func(root *TreeNode) int {
		if root == nil {
			return 0
		}
		left, right := dfs(root.Left), dfs(root.Right)
		if left > right {
			return left + 1
		} else {
			return right + 1
		}
	}
	m := dfs(root)
	n := int(math.Pow(2, float64(m)) - 1)
	var res [][]string
	for i := 0; i < m; i++ {
		v := []string{}
		for j := 0; j < n; j++ {
			v = append(v, "")
		}
		res = append(res, v)
	}

	var draw func(*TreeNode, int, int, int)
	draw = func(root *TreeNode, i int, l int, r int) {
		if root == nil {
			return
		}
		mid := (l + r) / 2
		res[i][mid] = strconv.Itoa(root.Val)
		draw(root.Left, i+1, l, mid)
		draw(root.Right, i+1, mid+1, r)
	}
	draw(root, 0, 0, len(res[0]))
	return res
}
