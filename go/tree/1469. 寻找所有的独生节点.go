package tree

func getLonelyNodes(root *TreeNode) []int {
	var dfs func(root *TreeNode)
	var res []int
	dfs = func(root *TreeNode) {
		if root == nil {
			return
		}
		if root.Left != nil && root.Right == nil {
			res = append(res, root.Left.Val)
		} else if root.Right != nil && root.Left == nil {
			res = append(res, root.Right.Val)
		}
		dfs(root.Left)
		dfs(root.Right)
	}
	dfs(root)
	return res
}
