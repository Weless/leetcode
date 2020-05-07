class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head,None
        while head:
            head = head.next
            cur.next = pre
            pre = cur
            cur = head
        return pre

# 递归解法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        ret = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return ret