package link

func insertionSortList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	newHead := &ListNode{Val: 0}
	newHead.Next = head
	sortedList, cur := head, head.Next
	for cur != nil {
		if sortedList.Val <= cur.Val {
			sortedList = sortedList.Next
		} else {
			pre := newHead
			for pre.Next.Val <= cur.Val {
				pre = pre.Next
			}
			sortedList.Next = cur.Next
			cur.Next = pre.Next
			pre.Next = cur
		}
		cur = sortedList.Next
	}
	return newHead.Next
}
