package tree

func distributeCoins(root *TreeNode) int {
	var dfs func(*TreeNode) int
	var res int
	dfs = func(root *TreeNode) int {
		if root == nil {
			return 0
		}
		left := dfs(root.Left)
		right := dfs(root.Right)

		if left < 0 {
			res += (-1 * left)
		} else {
			res += left
		}
		if right < 0 {
			res += (-1 * right)
		} else {
			res += right
		}
		return root.Val + left + right - 1
	}
	dfs(root)
	return res
}
