package link

func oddEvenList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	pre := head.Next
	odd, even := head, head.Next
	for even != nil && even.Next != nil {
		odd.Next = even.Next
		even.Next = even.Next.Next
		odd = odd.Next
		even = even.Next
	}
	odd.Next = pre
	return head
}
