package main

var res []int

func increasingBST(root *TreeNode) *TreeNode {
	res = make([]int, 0)
	dfs(root)
	node := &TreeNode{
		Val: res[0],
	}
	start := node
	for _, v := range res[1:] {
		next := &TreeNode{Val: v}
		node.Right = next
		node = node.Right
	}
	return start
}

func dfs(root *TreeNode) {
	if root != nil {
		dfs(root.Left)
		res = append(res, root.Val)
		dfs(root.Right)
	}
}
