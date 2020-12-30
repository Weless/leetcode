package main

func inorderSuccessor(root *TreeNode, p *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	if root.Val <= p.Val {
		return inorderSuccessor(root.Right, p)
	} else {
		left := inorderSuccessor(root.Left, p)
		if left != nil {
			return left
		} else {
			return root
		}
	}
}
