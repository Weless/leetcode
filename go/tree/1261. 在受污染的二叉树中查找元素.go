package tree

type FindElements struct {
	res  map[int]struct{}
	root *TreeNode
}

func Constructor(root *TreeNode) FindElements {
	f := FindElements{
		res: make(map[int]struct{}),
	}
	var dfs func(*TreeNode, int)
	dfs = func(root *TreeNode, i int) {
		if root == nil {
			return
		}
		root.Val = i
		f.res[root.Val] = struct{}{}
		dfs(root.Left, 2*i+1)
		dfs(root.Right, 2*i+2)
	}
	dfs(root, 0)
	f.root = root
	return f
}

func (this *FindElements) Find(target int) bool {
	if _, ok := this.res[target]; ok {
		return true
	}
	return false
}
