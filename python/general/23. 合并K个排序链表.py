class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pre = head = None
        i = 0
        while True:




    def min(self,lists:List[ListNode])->ListNode:
        if any(lists) == False:
            return None
        import sys
        _min = sys.maxsize
        i  = sys.maxsize
        for id,node in enumerate(lists):
            if node.val < _min:
                _min = node.val
                i = id
        return lists.pop(i)