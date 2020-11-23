package tree

func flipEquiv(root1 *TreeNode, root2 *TreeNode) bool {
	if root1 == root2 {
		return true
	}
	if root1 == nil || root2 == nil || root1.Val != root2.Val {
		return false
	}
	one := flipEquiv(root1.Left, root2.Left) && flipEquiv(root1.Right, root2.Right)
	two := flipEquiv(root1.Left, root2.Right) && flipEquiv(root1.Right, root2.Left)
	return one || two
}
