package tree

import "fmt"

func delNodes(root *TreeNode, to_delete []int) []*TreeNode {
	var dfs func(*TreeNode) *TreeNode
	s := make(map[int]struct{})
	var res []*TreeNode
	for _, v := range to_delete {
		s[v] = struct{}{}
	}
	dfs = func(root *TreeNode) *TreeNode {
		if root == nil {
			return nil
		}
		v := root.Val
		if containValue(s, v) {
			if root.Left != nil {
				if !containValue(s, root.Left.Val) {
					fmt.Println(1)
					res = append(res, root.Left)
				}
				dfs(root.Left)
			}
			if root.Right != nil {
				if !containValue(s, root.Right.Val) {
					fmt.Println(1)
					res = append(res, root.Right)
				}
				dfs(root.Right)
			}
			return nil
		}
		root.Left = dfs(root.Left)
		root.Right = dfs(root.Right)
		return root
	}
	dfs(root)
	if root != nil && !containValue(s, root.Val) {
		res = append(res, root)
	}
	return res
}

func containValue(s map[int]struct{}, v int) bool {
	if _, ok := s[v]; ok {
		return true
	}
	return false
}
