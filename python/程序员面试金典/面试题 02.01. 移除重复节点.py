class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        s = set()
        cur, pre = head.next, head
        s.add(pre.val)
        while cur:
            if cur.val not in s:
                s.add(cur.val)
                cur = cur.next
                pre = pre.next
            else:
                pre.next = cur.next
                cur = cur.next
        return head
        