# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        tmp = []
        while head != None:
            tmp.append(head.val)
            head = head.next
        l = len(tmp)
        result = 0
        for i,v in enumerate(tmp):
            result += v*2**(l-1-i)
        return result



class Solution2:
    def getDecimalValue(self, head: ListNode) -> int:
        re = 0
        tmp = head
        while tmp is not None:
            re = (re << 1) | tmp.val # rec = rec * 2 + head.val
            tmp = tmp.next
        return re

