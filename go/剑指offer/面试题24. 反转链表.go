package main

func reverseList(head *ListNode) *ListNode {
	pre := new(ListNode)
	pre = nil
	cur := head
	for head != nil {
		head = head.Next
		cur.Next = pre
		pre = cur
		cur = head
	}
	return pre
}
