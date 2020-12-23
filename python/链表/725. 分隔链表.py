from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        res = []
        cur = root
        while cur:
            res.append(cur.val)
            cur = cur.next
        l = len(cur)

