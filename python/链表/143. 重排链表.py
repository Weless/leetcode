# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        l = 0
        p = head
        while p:
            l+=1
            p = p.next
        if l % 2 == 0:
            start,end = [],[]
            i = 0
            p = head
            while i < l//2:
                start.append(p)
                p = p.next
                i+=1
            while i <= l:
                end.append(p)
                p = p.next
                i+=1
            while start or end:
                start
        else: