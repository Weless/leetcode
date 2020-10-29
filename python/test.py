from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]



