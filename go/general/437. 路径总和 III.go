package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func count(node *TreeNode, sum int) int {
	if node == nil {
		return 0
	}
	isMe := 0
	if node.Val == sum {
		isMe = 1
	}
	leftCount := count(node.Left, sum-node.Val)
	rightCount := count(node.Right, sum-node.Val)
	return isMe + leftCount + rightCount
}

func pathSum(root *TreeNode, sum int) int {
	if root == nil {
		return 0
	}
	return count(root, sum) + pathSum(root.Left, sum) + pathSum(root.Right, sum)
}
