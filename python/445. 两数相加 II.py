# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1,num2 = 0,0
        while l1:
            num1*=10
            num1+=l1.val
        while l2:
            num2*=10
            num2+=l2.val
        theSum = num1 + num2
        theSum_str = str(theSum)
        firstNode = ListNode(theSum_str[0])
        next = firstNode
        if len(theSum_str)>1:
            for i in theSum_str[1:]:
                next.next = ListNode(int(i))
                next = next.next
        return firstNode

# 栈，链表中数位的顺序与我们做加法的顺序是相反的，为了逆序处理所有数位，我们可以使用栈
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        ans = None
        carry = 0
        while s1 or s2 or carry != 0:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            cur = a + b + carry
            carry = cur // 10
            cur %= 10
            curnode = ListNode(cur)
            curnode.next = ans
            ans = curnode
        return ans
