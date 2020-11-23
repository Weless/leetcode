package tree

func subtreeWithAllDeepest(root *TreeNode) *TreeNode {
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
	left, right := dfs(root.Left), dfs(root.Right)
	if left == right {
		return root
	} else if left > right {
		return subtreeWithAllDeepest(root.Left)
	} else {
		return subtreeWithAllDeepest(root.Right)
	}
}
