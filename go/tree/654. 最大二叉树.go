package tree

import "math"

func constructMaximumBinaryTree(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}
	i := getMaxIndex(nums)
	node := &TreeNode{Val: nums[i]}
	node.Left = constructMaximumBinaryTree(nums[:i])
	node.Right = constructMaximumBinaryTree(nums[i+1:])
	return node
}

func getMaxIndex(A []int) int {
	index, max := 0, math.MinInt32
	for i, v := range A {
		if v > max {
			max = v
			index = i
		}
	}
	return index
}
