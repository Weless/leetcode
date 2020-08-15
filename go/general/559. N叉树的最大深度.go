package main

import "math"

func maxDepth(root *Node) int {
	if root == nil {
		return 0
	}
	if len(root.Children) == 0 {
		return 1
	}
	var height []int
	for _, v := range root.Children {
		height = append(height, maxDepth(v))
	}
	return max(height) + 1
}

func max(h []int) int {
	_max := -1
	for _, v := range h {
		if v > _max {
			_max = v
		}
	}
	return _max
}
