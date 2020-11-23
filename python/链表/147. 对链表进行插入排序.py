class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# start指向部分有序的链表
# 当出现链表节点逆序的情况，出现逆序的节点插入到start指向的部分有序的链接中
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head: return head
        start = head
        cur = head.next
        pre = head
        while cur:
            # 需要调整节点顺序
            if cur.val < pre.val:
                tmp = cur
                p = None
                c = start
                while c and tmp.val >= c.val:
                    c = c.next
                    if not p: p = start
                    else: p = p.next
                cur = cur.next
                pre.next = cur
                # 乱序节点值比有序链表第一个值小
                if not p:
                    tmp.next = start
                    start = tmp
                else:
                    p.next = tmp
                    tmp.next = c
            else:
                cur = cur.next
                pre = pre.next
        return start
