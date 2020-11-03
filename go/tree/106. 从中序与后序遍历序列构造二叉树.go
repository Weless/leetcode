package tree

func buildTree(inorder []int, postorder []int) *TreeNode {
	if len(inorder) == 0 {
		return nil
	}
	node := &TreeNode{Val: postorder[len(postorder)-1]}
	i := getIndex(inorder, node.Val)
	node.Left = buildTree(inorder[:i], postorder[:i])
	node.Right = buildTree(inorder[i+1:], postorder[i:len(postorder)-1])
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
