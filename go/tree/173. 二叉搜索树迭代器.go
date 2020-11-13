package tree

type BSTIterator struct {
	stack []*TreeNode
}

func Constructor(root *TreeNode) BSTIterator {
	bt := BSTIterator{
		stack: make([]*TreeNode, 100),
	}
	bt.leftMostInOrder(root)
	return bt
}

func (this *BSTIterator) leftMostInOrder(root *TreeNode) {
	for root.Left != nil {
		this.stack = append(this.stack, root)
		root = root.Left
	}
}

/** @return the next smallest number */
func (this *BSTIterator) Next() int {
	tmp_node := this.stack[len(this.stack)-1]
	this.stack = this.stack[:len(this.stack)-1]

	if tmp_node.Right != nil {
		this.leftMostInOrder(tmp_node.Right)
	}
	return tmp_node.Val
}

/** @return whether we have a next smallest number */
func (this *BSTIterator) HasNext() bool {
	return len(this.stack) > 0
}
