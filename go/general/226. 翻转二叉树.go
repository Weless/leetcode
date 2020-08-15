package main

func invertTree(root *TreeNode) *TreeNode {
	if root == nil{
		return nil
	}
	left := invertTree(root.Left)
	right:=invertTree(root.Right)
	root.Right,root.Left = left,right
	return root
}
