class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre,cur = None,head
        while cur:
            if cur.val == val:
                if pre:
                    pre.next = cur.next
                    cur = cur.next
                else:
                    cur = cur.next
                    head = cur
            else:
                pre = cur
                cur = cur.next
        return head

