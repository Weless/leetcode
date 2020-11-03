package tree

import "strconv"

func findDuplicateSubtrees(root *TreeNode) []*TreeNode {
	var dfs func(*TreeNode) string
	var res []*TreeNode
	d := make(map[string]int)
	dfs = func(root *TreeNode) string {
		if root == nil {
			return "#"
		}
		left := dfs(root.Left)
		right := dfs(root.Right)
		subTree := left + "," + right + "," + strconv.Itoa(root.Val)
		d[subTree] += 1

		if d[subTree] == 2 {
			res = append(res, root)
		}
		return subTree
	}
	dfs(root)
	return res
}
