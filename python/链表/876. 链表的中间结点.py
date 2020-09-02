class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cur,pre = head,head
        while cur.next and cur.next.next:
            cur = cur.next.next
            pre = pre.next
        if cur.next:
            return pre.next
        return pre