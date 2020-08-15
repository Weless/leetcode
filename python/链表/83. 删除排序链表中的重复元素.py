class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur = cur.next.next
            else:
                cur = cur.next
        return head
