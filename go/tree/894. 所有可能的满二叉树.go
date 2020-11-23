package tree

var d = map[int][]*TreeNode{
	0: []*TreeNode{},
	1: []*TreeNode{&TreeNode{Val: 0}},
}

func allPossibleFBT(N int) []*TreeNode {
	if _, ok := d[N]; !ok {
		var res []*TreeNode
		for i := 0; i < N; i++ {
			j := N - 1 - i
			for _, left := range allPossibleFBT(i) {
				for _, right := range allPossibleFBT(j) {
					root := &TreeNode{Val: 0}
					root.Left = left
					root.Right = right
					res = append(res, root)
				}
			}
		}
		d[N] = res
	}
	return d[N]
}
