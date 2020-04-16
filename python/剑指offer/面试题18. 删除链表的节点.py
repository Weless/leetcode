# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:

        if head.next is None and head.val == val:
            head = None
            return head
        if head.next != None and head.val == val:
            return head.next
        pre = ListNode(0)
        result = head
        while head:
            if head.val == val:
                head = head.next
                pre.next = head
            else:
                pre,head = head,head.next
        return result
