package tree

import "sort"

func bstFromPreorder(preorder []int) *TreeNode {
	if len(preorder) == 0 {
		return nil
	}
	inorder := make([]int, len(preorder))
	copy(inorder, preorder)
	sort.Ints(inorder)
	pre_val := preorder[0]
	node := &TreeNode{Val: pre_val}
	index := 0
	for i, v := range inorder {
		if v == pre_val {
			index = i
			break
		}
	}
	node.Left = bstFromPreorder(preorder[1 : index+1])
	node.Right = bstFromPreorder(preorder[index+1:])
	return node
}
