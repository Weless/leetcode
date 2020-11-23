package tree

func lcaDeepestLeaves(root *TreeNode) *TreeNode {
	var dfs func(*TreeNode) int
	dfs = func(root *TreeNode) int {
		if root == nil {
			return 0
		}
		left := dfs(root.Left)
		right := dfs(root.Right)
		if left > right {
			return 1 + left
		} else {
			return 1 + right
		}
	}

	left, right := dfs(root.Left), dfs(root.Right)
	if left == right {
		return root
	} else if left > right {
		return lcaDeepestLeaves(root.Left)
	} else {
		return lcaDeepestLeaves(root.Right)
	}
}
