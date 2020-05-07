package main

// 后序遍历

func isBalanced(root *TreeNode) bool {
	return recur(root) != -1
}

func recur(root *TreeNode) int {
	if root == nil {
		return 0
	}
	left := recur(root.Left)
	if left == -1 {
		return -1
	}
	right := recur(root.Right)
	if right == -1 {
		return -1
	}
	if abs(left-right) > 1 {
		return -1
	} else {
		return max(left, right) + 1
	}
}

func abs(a int) int {
	if a < 0 {
		return -1 * a
	} else {
		return a
	}
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

// 先序遍历
// func isBalanced(root *TreeNode) bool {
// 	if root == nil {
// 		return true
// 	}
// 	return abs(maxDepth(root.Left)-maxDepth(root.Right)) <= 1 && isBalanced(root.Left) && isBalanced(root.Right)
// }
//
// func depth(root *TreeNode) int {
// 	if root == nil {
// 		return 0
// 	}
// 	return max(depth(root.Left), depth(root.Right)) + 1
// }
//

//
