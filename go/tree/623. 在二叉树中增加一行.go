package tree

func addOneRow(root *TreeNode, v int, d int) *TreeNode {
	if d == 1 {
		node := &TreeNode{Val: v}
		node.Left = root
		return node
	}
	var dfs func(*TreeNode, int)
	dfs = func(root *TreeNode, n int) {
		if root == nil {
			return
		}
		if n+1 == d {
			if root.Left != nil {
				node := &TreeNode{Val: v}
				node.Left = root.Left
				root.Left = node
			} else {
				node := &TreeNode{Val: v}
				root.Left = node
			}
			if root.Right != nil {
				node := &TreeNode{Val: v}
				node.Right = root.Right
				root.Right = node
			} else {
				node := &TreeNode{Val: v}
				root.Right = node
			}
		}
		dfs(root.Left, n+1)
		dfs(root.Right, n+1)
	}
	dfs(root, 1)
	return root
}
