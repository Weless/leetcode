package tree

func pseudoPalindromicPaths(root *TreeNode) int {
	var dfs func(*TreeNode, []int)
	var res [][]int
	var path []int
	dfs = func(root *TreeNode, path []int) {
		if root == nil {
			return
		}
		path = append(path, root.Val)
		if root.Left == nil && root.Right == nil {
			tmp := make([]int, len(path))
			copy(tmp, path)
			res = append(res, tmp)
		}
		dfs(root.Left, path)
		dfs(root.Right, path)
		path = path[:len(path)-1]
	}
	dfs(root, path)
	r := 0
	for _, p := range res {
		if isFakePalindrome(p) {
			r++
		}
	}
	return r
}

func isFakePalindrome(path []int) bool {
	counter := make(map[int]int)
	for _, v := range path {
		counter[v]++
	}
	c := 0
	for _, v := range counter {
		if v%2 != 0 {
			c++
		}
		if c == 2 {
			return false
		}
	}
	return true
}
