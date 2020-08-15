class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur = head
        mid = self.findMidNode(cur)
        cur2 = self.transLink(mid.next)
        print(cur2)
        cur1 = head
        while cur2:
            if cur1.val != cur2.val: return False
            cur1 = cur1.next
            cur2 = cur2.next
        return True
    # 反转链表
    def transLink(self,head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
    # 找到链表的中间节点
    def findMidNode(self,head):
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow