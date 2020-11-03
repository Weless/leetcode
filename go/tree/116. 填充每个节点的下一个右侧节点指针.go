package tree

type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

// DFS
func connect(root *Node) *Node {
	if root == nil {
		return nil
	}
	connectTwoNode(root.Left, root.Right)
	return root
}

func connectTwoNode(node1, node2 *Node) {
	if node1 == nil || node2 == nil {
		return
	}
	node1.Next = node2
	connectTwoNode(node1.Left, node1.Right)
	connectTwoNode(node2.Left, node2.Right)
	connectTwoNode(node1.Right, node2.Left)
}

// BFS
func connect2(root *Node) *Node {
	if root == nil {
		return nil
	}
	q := []*Node{}
	q = append(q, root)
	for len(q) != 0 {
		size := len(q)
		for i := 0; i < size; i++ {
			node := q[0]
			q = q[1:]
			if node.Left != nil {
				q = append(q, node.Left)
			}
			if node.Right != nil {
				q = append(q, node.Right)
			}
			if i < size-1 {
				node.Next = q[0]
			}
		}
	}
	return root
}
