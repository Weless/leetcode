package main

import (
	"fmt"
	"reflect"
)

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	var f func(*TreeNode, *[]int)
	f = func(root *TreeNode, res *[]int) {
		if root != nil {
			if root.Left == nil && root.Right == nil {
				*res = append(*res, root.Val)
			}
			f(root.Left, res)
			f(root.Right, res)
		}
	}

	var res1 []int
	var res2 []int
	f(root1, &res1)
	f(root2, &res2)
	fmt.Println(res1)
	fmt.Println(res2)
	return reflect.DeepEqual(res1, res2)
}
