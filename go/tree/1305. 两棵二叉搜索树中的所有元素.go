package tree

func getAllElements(root1 *TreeNode, root2 *TreeNode) []int {
	var dfs func(*TreeNode, *[]int)
	res1, res2 := []int{}, []int{}
	dfs = func(root *TreeNode, res *[]int) {
		if root == nil {
			return
		}
		dfs(root.Left, res)
		*res = append(*res, root.Val)
		dfs(root.Right, res)
	}
	dfs(root1, &res1)
	dfs(root2, &res2)
	var res []int
	i, j := 0, 0
	for i < len(res1) && j < len(res2) {
		if res1[i] < res2[j] {
			res = append(res, res1[i])
			i++
		} else {
			res = append(res, res2[j])
			j++
		}
	}
	if i < len(res1) {
		res = append(res, res1[i:]...)
	}
	if j < len(res2) {
		res = append(res, res2[j:]...)
	}
	return res
}
