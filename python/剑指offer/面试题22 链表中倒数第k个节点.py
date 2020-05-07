# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        p1,p2 = head,head
        while k:
            p2 = p2.next
            k-=1
        while p2:
            p2 = p2.next
            p1 = p1.next
        return p1
