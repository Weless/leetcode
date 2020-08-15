package main

// 递归
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	parent_val := root.Val
	p_val := p.Val
	q_val := q.Val
	if p_val < parent_val && q_val < parent_val {
		return lowestCommonAncestor(root.Left, p, q)
	} else if p.Val > parent_val && q_val > parent_val {
		return lowestCommonAncestor(root.Right, p, q)
	} else {
		return root
	}
}

// 循环
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	p_val := p.Val
	q_val := q.Val
	for root != nil {
		if p_val < root.Val && q.Val < root.Val {
			root = root.Left
		} else if p_val > root.Val && q_val > root.Val {
			root = root.Right
		} else {
			return root
		}
	}
	return root
}
