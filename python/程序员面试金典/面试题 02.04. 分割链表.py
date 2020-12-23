class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 记录基准点和基准点之前的位置
        core_pre, core = None, None
        start = ListNode(-1)
        start.next = head
        cur = start.next
        pre = start
        while cur:
            # 先找到第一个大于等于x的点，作为基准点
            if not core and cur.val >= x:
                core = cur
                core_pre = pre
                cur = cur.next
                pre = pre.next
                continue
            # 将小于x的点都移动到基准点之前
            if core and cur.val < x:
                # 将该点从链表中提取出来，并用tmp保存
                tmp = cur
                pre.next = cur.next
                cur = cur.next

                # 将该点链接到基准点之前
                core_pre.next = tmp
                tmp.next = core
                core_pre = core_pre.next
                continue

            # 其他情况
            cur = cur.next
            pre = pre.next
        return start.next

