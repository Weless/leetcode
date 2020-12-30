package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func convertBiNode(root *TreeNode) *TreeNode {
	pre := &TreeNode{}
	head := pre
	dfs(root, pre)
	return head.Right
}

func dfs(root *TreeNode, pre *TreeNode) *TreeNode {
	if root == nil {
		return pre
	}
	pre = dfs(root.Left, pre)
	root.Left = nil
	pre.Right = root
	pre = root
	pre = dfs(root.Right, pre)
	return pre
}
