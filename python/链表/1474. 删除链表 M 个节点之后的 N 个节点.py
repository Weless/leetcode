class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        start = ListNode(-1)
        start.next = head
        pre,cur = start,start.next
        while cur:
            i = 0
            while cur and i != m:
                cur = cur.next
                pre = pre.next
                i+=1
            i = 0
            while cur and i != n:
                cur = cur.next
                i+=1
            pre.next = cur
        return head