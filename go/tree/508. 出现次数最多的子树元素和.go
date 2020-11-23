package tree

func findFrequentTreeSum(root *TreeNode) []int {
	var dfs func(*TreeNode) int
	d := make(map[int]int)
	var res []int
	var mostFreq int

	dfs = func(root *TreeNode) int {
		if root == nil {
			return 0
		}
		sum := root.Val + dfs(root.Left) + dfs(root.Right)
		d[sum]++
		if d[sum] > mostFreq {
			mostFreq = d[sum]
		}
		return sum
	}

	dfs(root)

	for k, v := range d {
		if v == mostFreq {
			res = append(res, k)
		}
	}
	return res
}
