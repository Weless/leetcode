class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# my way
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head : return head
        pre,cur = head,head.next
        last = None
        while cur:
            pre.next = cur.next
            cur.next = pre
            if not last:
                head = cur
                last = pre
            else:
                last.next = cur
                last = pre
            if pre.next:
                cur = pre.next.next
                pre = pre.next
            else:
                break
        return head

# iterative operation
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        DummyHead = ListNode(-1)
        DummyHead.next = head
        tmp = DummyHead
        while tmp.next and tmp.next.next:
            node1 = tmp.next
            node2 = tmp.next.next
            tmp.next = node2
            node1.next = node2.next
            node2.next = node1
            tmp = node1
        return DummyHead.next

# recersive
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead
