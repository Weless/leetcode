package main

func getKthFromEnd(head *ListNode, k int) *ListNode {
	p1, p2 := head, head
	for k > 0 {
		p2 = p2.Next
		k -= 1
	}
	for p2 != nil {
		p2 = p2.Next
		p1 = p1.Next
	}
	return p1
}
