package main

import "fmt"

var res []int

func isUnivalTree(root *TreeNode) bool {
	res := make([]int, 0)
	dfs(root)
	fmt.Println(res)
	if len(res) == 1 {
		return true
	} else {
		return false
	}
}

func dfs(root *TreeNode) {
	if root != nil {
		if !inResult(res, root.Val) {
			res = append(res, root.Val)
		}
		dfs(root.Left)
		dfs(root.Right)
	}
}

func inResult(result []int, k int) bool {
	for _, v := range result {
		if v == k {
			return true
		}
	}
	return false
}
