class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = tmp = ListNode(0)

        while l1 and l2:
            if l1.val > l2.val:
                l3.next = l2
                l2 = l2.next
            else:
                l3.next = l1
                l1 = l1.next
            l3 = l3.next

        if l1:
            l3.next = l1
        if l2:
            l3.next = l2
        return tmp.next

# 递归
# 1.当链表1为空链表时，直接返回链表2；当链表2为空链表时，返回链表1。这两种情况都是递归的边界。
# 2.当链表1和链表2均不为空时，找出两个链表头节点中值较小者作为新链表的头节点，对于剩余的部分使用递归求解。

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not  l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
