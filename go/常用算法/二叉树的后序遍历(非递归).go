package algorithem

func postorderTraversal(root *TreeNode) []int {
	var res []int
	var stack []*TreeNode
	for len(stack) != 0 || root != nil {
		for root != nil {
			res = append(res, root.Val)
			stack = append(stack, root)
			root = root.Right
		}
		if len(stack) != 0 {
			t := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			root = t.Left
		}
	}
	return reverse(res)
}

func reverse(A []int) []int {
	var res []int
	for i := len(A) - 1; i >= 0; i-- {
		res = append(res, A[i])
	}
	return res
}
