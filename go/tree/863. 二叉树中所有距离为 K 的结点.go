package tree

func distanceK(root *TreeNode, target *TreeNode, K int) []int {
	var subTreeAdd func(*TreeNode, int)
	var dfs func(*TreeNode) int
	var ans []int
	dfs = func(root *TreeNode) int {
		if root == nil {
			return -1
		}
		if root == target {
			subTreeAdd(root, 0)
			return 1
		} else {
			left, right := dfs(root.Left), dfs(root.Right)
			if left != -1 {
				if left == K {
					ans = append(ans, root.Val)
				}
				subTreeAdd(root.Right, left+1)
				return left + 1
			} else if right != -1 {
				if right == K {
					ans = append(ans, root.Val)
				}
				subTreeAdd(root.Left, right+1)
				return right + 1
			} else {
				return -1
			}
		}
	}
	subTreeAdd = func(root *TreeNode, dist int) {
		if root == nil {
			return
		}
		if dist == K {
			ans = append(ans, root.Val)
		} else {
			subTreeAdd(root.Left, dist+1)
			subTreeAdd(root.Right, dist+1)
		}
	}
	dfs(root)
	return ans
}
