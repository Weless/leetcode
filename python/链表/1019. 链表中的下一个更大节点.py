from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res = []
        max = 0
        while head:
            cur = head
            ok = False
            while cur:
                if cur.val > max:
                    max = cur.val
                if max != 0 and head.val < max:
                    res.append(max)
                    ok = True
                    break
                if max == 0 and head.val < cur.val:
                    max = cur.val
                    res.append(max)
                    ok = True
                    break
                cur = cur.next
            if not ok:
                res.append(0)
                max = 0
            head = head.next
        return res
def buildList(a):
    head = ListNode(-1)
    cur = head
    for i in a:
        head.next = ListNode(i)
        head = head.next
    return cur.next

s = Solution()
print(s.nextLargerNodes(buildList([1,7,5,1,9,2,5,1])))