class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return None
        odd,even,cur = head,head.next,ListNode(-1)
        while odd and odd.next:
            cur.next = odd
            cur = cur.next
            odd = odd.next.next

