package tree

func kthSmallest(root *TreeNode, k int) int {
	var dfs func(*TreeNode)
	var res int
	count := 0
	dfs = func(root *TreeNode) {
		if root == nil {
			return
		}
		dfs(root.Left)
		count++
		if count == k {
			res = root.Val
			return
		}
		dfs(root.Right)
	}
	dfs(root)
	return res
}
