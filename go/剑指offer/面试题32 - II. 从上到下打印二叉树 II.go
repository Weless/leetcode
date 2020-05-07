package main

func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	queue := []*TreeNode{root}
	var res [][]int
	for len(queue) > 0 {
		var tmp []int
		l := len(queue)
		for i := 0; i < l; i += 1 {
			node := queue[0]
			tmp = append(tmp, node.Val)
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
			queue = queue[1:]
		}
		res = append(res, tmp)
	}
	return res
}
