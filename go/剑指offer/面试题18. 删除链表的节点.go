package main

func deleteNode(head *ListNode, val int) *ListNode {
	cur := head
	if cur.Val == val {
		return head.Next
	}
	pre := head
	cur = cur.Next
	for cur != nil {
		if cur.Val == val {
			pre.Next = cur.Next
			cur = cur.Next
		} else {
			pre = pre.Next
			cur = cur.Next
		}
	}
	return head
}
