class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
# BFS
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        from collections import deque
        q = deque()
        q.appendleft(root)
        while q:
            last = None
            for i in range(len(q)):
                node = q.pop()
                if node.left: q.appendleft(node.left)
                if node.right: q.appendleft(node.right)
                if i == 0:
                    last = node
                    continue
                last.next = node
                last = node
        return root

# BFS优化空间复杂度
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        cur = root
        while cur:
            dummy = Node(0)
            # pre指向下一层节点的前一个节点
            pre = dummy
            # 然后开始遍历当前层的链表
            while cur:
                if cur.left:
                    pre.next = cur.left
                    pre = pre.next
                if cur.right:
                    pre.next = cur.right
                    pre = pre.next
                # 沿着当前层移动
                cur = cur.next
            # 到达下一层
            cur = dummy.next
        return root

