package tree

func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}
	node := &TreeNode{Val: preorder[0]}
	i := getIndex(inorder, node.Val)
	node.Left = buildTree(preorder[1:i+1], inorder[:i])
	node.Right = buildTree(preorder[i+1:], inorder[i+1:])
	return node
}

func getIndex(A []int, value int) int {
	for i, v := range A {
		if value == v {
			return i
		}
	}
	return 0
}
