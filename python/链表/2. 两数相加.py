# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(-1)
        cur = head
        while l1 or  l2:
            v1,v2 = 0,0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            sum = v1 + v2 + carry
            sum,carry = sum % 10 , sum //10
            head.next = ListNode(sum)
            head = head.next
        if carry:
            head.next = ListNode(carry)
        return cur