package main

func averageOfLevels(root *TreeNode) []float64 {
	if root == nil {
		return nil
	}
	var queue []*TreeNode
	queue = append(queue, root)
	var res []float64
	for len(queue) != 0 {
		var tmp []int
		l := len(queue)
		for i := 0; i < l; i++ {
			node := queue[0]
			tmp = append(tmp, node.Val)
			queue = queue[1:]
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		res = append(res, float64(sum(tmp))/float64(len(tmp)))
	}
	return res
}
func sum(t []int) int {
	res := 0
	for _, v := range t {
		res += v
	}
	return res
}
