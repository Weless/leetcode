package link

func isPalindrome(head *ListNode) bool {
	var res []int
	for head != nil {
		res = append(res, head.Val)
		head = head.Next
	}
	return helper(res)

}

func helper(A []int) bool {
	for i, j := 0, len(A)-1; i < j; i, j = i+1, j-1 {
		if A[i] != A[j] {
			return false
		}
	}
	return true
}
