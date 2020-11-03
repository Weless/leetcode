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
        q.append(root)
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                if i != size -1:
                    node.next = q[0]
        return root

# DFS
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        self.connectTwoNode(root.left,root.right)
        return root
    def connectTwoNode(self,node1,node2):
        if not node1 or not node2:
            return
        # 将传入的两个节点连接
        node1.next = node2
        # 连接相同父节点的两个子节点
        self.connectTwoNode(node1.left,node1.right)
        self.connectTwoNode(node2.left,node2.right)
        # 连接跨越父节点的两个子节点
        self.connectTwoNode(node1.right,node2.left)