package main

type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

func copyRandomList(head *Node) *Node {
	if head == nil {
		return head
	}

	cur := head
	for cur != nil {
		cloned := &Node{cur.Val, nil, nil}
		cloned.Next = cur.Next
		cur.Next = cloned
		cur = cur.Next.Next
	}

	cur = head
	for cur != nil {
		cloned := cur.Next
		if cur.Random != nil {
			cloned.Random = cur.Random.Next
		}
		cur = cloned.Next
	}

	cur = head
	newHead, cloned := cur.Next, cur.Next
	for cur != nil {
		cur.Next = cloned.Next
		cur = cur.Next
		if cur != nil {
			cloned.Next = cur.Next
		}
		cloned = cloned.Next
	}
	return newHead
}
