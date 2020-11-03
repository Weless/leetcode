package tree

import "math"

func minDiffInBST(root *TreeNode) int {
	pre, cur := math.MinInt32, math.MaxInt32
	var dfs func(root *TreeNode)
	dfs = func(root *TreeNode) {
		if root == nil {
			return
		}
		dfs(root.Left)
		cur = min(cur, root.Val-pre)
		pre = root.Val
		dfs(root.Right)
	}
	dfs(root)
	return cur
}

func min(A, B int) int {
	if A < B {
		return A
	} else {
		return B
	}
}
