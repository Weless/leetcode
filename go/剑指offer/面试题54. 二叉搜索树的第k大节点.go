package main

var res int
var tmp int
func kthLargest(root *TreeNode, k int) int {
	tmp = k
	dfs(root)
	return res
}

func dfs(root *TreeNode)  {
	if root != nil{
		dfs(root.Right)
		tmp--
		if tmp == 0{
			res = root.Val
			return
		}
		dfs(root.Left)
	}
}
