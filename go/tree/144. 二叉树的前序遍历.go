package tree

func preorderTraversal(root *TreeNode) []int {
	var res []int
	var stack []*TreeNode
	for len(stack) != 0 || root != nil {
		for root != nil {
			res = append(res, root.Val)
			stack = append(stack, root)
			root = root.Left
		}
		if len(stack) != 0 {
			t := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			root = t.Right
		}
	}
	return res
}
