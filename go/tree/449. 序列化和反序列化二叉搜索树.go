package tree

import (
	"fmt"
	"strconv"
	"strings"
)

type Codec struct {
}

func Constructor() Codec {
	return Codec{}
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
	var dfs func(*TreeNode) string
	dfs = func(root *TreeNode) string {
		if root == nil {
			return ""
		}
		left := dfs(root.Left)
		right := dfs(root.Right)
		return strconv.Itoa(root.Val) + " " + left + " " + right
	}
	return dfs(root)
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
	tmp := strings.Split(data, " ")
	var res []int
	for _, v := range tmp {
		if v == "" {
			continue
		}
		vint, _ := strconv.Atoi(v)
		res = append(res, vint)
	}
	fmt.Println(res)
	var helper func([]int) *TreeNode
	helper = func(res []int) *TreeNode {
		if len(res) == 0 {
			return nil
		}
		fmt.Printf("root:%d\n", res[0])
		root := &TreeNode{Val: res[0]}
		var left []int
		var right []int
		for _, v := range res {
			if v < res[0] {
				left = append(left, v)
			} else if v > res[0] {
				right = append(right, v)
			}
		}
		fmt.Printf("left:%v\n", left)
		fmt.Printf("right:%v\n", right)
		root.Left = helper(left)
		root.Right = helper(right)
		return root
	}
	return helper(res)
}
