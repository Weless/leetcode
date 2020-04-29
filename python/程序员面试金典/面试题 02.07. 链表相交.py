class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        while headA and headB:
            if headA == headB:
                return headA

            if not headA:
                headA = headB
            if not headB:
                headB = headA
            headA = headA.next
            headB = headB.next
