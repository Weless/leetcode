package main

func reverseList(head *ListNode) *ListNode {
	var pre *ListNode
	cur := head
	for head != nil {
		head = head.Next
		cur.Next = pre
		pre = cur
		cur = head
	}
	return pre
}
