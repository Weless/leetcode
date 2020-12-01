package tree

func longestUnivaluePath(root *TreeNode) int {
	var dfs func(*TreeNode) int
	var ans int
	dfs = func(root *TreeNode) int {
		if root == nil {
			return 0
		}
		tmp := 0
		left := dfs(root.Left)
		right := dfs(root.Right)
		if root.Left != nil && root.Right != nil && root.Val == root.Left.Val && root.Val == root.Right.Val {
			v := left + right + 2
			if v > ans {
				ans = v
			}
		}
		if root.Left != nil && root.Left.Val == root.Val {
			tmp = left + 1
		}
		if root.Right != nil && root.Right.Val == root.Val {
			v := right + 1
			if v > tmp {
				tmp = v
			}
		}
		if tmp > ans {
			ans = tmp
		}
		return tmp
	}
	dfs(root)
	return ans
}
