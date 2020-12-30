class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        pre,cur=None,list1
        i = 1
        while cur:
            if i == a:
                while cur and i <= b:
                    cur = cur.next
                    i+=1
                break
            if pre == None:
                pre = cur
            else:
                pre = pre.next
            cur = cur.next
            i+=1
        pre.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = cur
        return list1