package link

func mergeInBetween(list1 *ListNode, a int, b int, list2 *ListNode) *ListNode {
	var pre *ListNode
	cur := list1
	i := 0
	for cur != nil {
		if i == a {
			for cur != nil && i <= b {
				cur = cur.Next
				i += 1
			}
			break
		}
		if pre == nil {
			pre = cur
		} else {
			pre = pre.Next
		}
		cur = cur.Next
		i += 1
	}
	pre.Next = list2
	for list2.Next != nil {
		list2 = list2.Next
	}
	list2.Next = cur
	return list1
}
