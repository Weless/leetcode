package main

func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	queue := []*TreeNode{root}
	var res [][]int
	var j int
	for len(queue) > 0 {
		l := len(queue)
		var tmp []int
		for i := 0; i < l; i++ {
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
		if j%2 == 0 {
			res = append(res, tmp)
		} else {
			reverse(tmp)
			res = append(res, tmp)
		}
	}
	return res
}

func reverse(tmp []int) {
	for i, j := 0, len(tmp)-1; i < j; i, j = i+1, j-1 {
		tmp[i], tmp[j] = tmp[j], tmp[i]
	}
}
