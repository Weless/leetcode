package tree

func flatten(root *TreeNode) {
	if root == nil {
		return
	}
	flatten(root.Left)
	flatten(root.Right)

	tmp := root.Right
	root.Right = tmp
	root.Left = nil

	p := root
	for p.Right != nil {
		p = p.Right
	}
	p.Right = tmp
}
