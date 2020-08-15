class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        cur = head
        while k:
            head = head.next
            k-=1
        while head:
            head = head.next
            cur = cur.next
        return cur.val