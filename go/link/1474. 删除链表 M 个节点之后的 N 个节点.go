package link

func deleteNodes(head *ListNode, m int, n int) *ListNode {
	start := &ListNode{Val: -1}
	start.Next = head
	pre, cur := start, start.Next
	for cur != nil {
		i := 0
		for cur != nil && i != m {
			cur = cur.Next
			pre = pre.Next
			i++
		}
		i = 0
		for cur != nil && i != n {
			cur = cur.Next
			i++
		}
		pre.Next = cur
	}
	return head
}
