package tree

func connect(root *Node) *Node {
	if root == nil {
		return nil
	}
	cur := root
	for cur != nil {
		dummy := &Node{Val: 0}
		pre := dummy
		for cur != nil {
			if cur.Left != nil {
				pre.Next = cur.Left
				pre = pre.Next
			}
			if cur.Right != nil {
				pre.Next = cur.Right
				pre = pre.Next
			}
			cur = cur.Next
		}
		cur = dummy.Next
	}
	return root
}
