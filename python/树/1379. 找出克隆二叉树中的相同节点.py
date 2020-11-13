class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# BFS
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        from collections import deque
        q1,q2 = deque(),deque()
        q1.appendleft(original)
        q2.appendleft(cloned)
        while q1 and q2:
            node1 = q1.pop()
            node2 = q2.pop()
            if node1.val == target.val:
                return node2
            if node1.left: q1.appendleft(node1.left)
            if node1.right: q1.appendleft(node1.right)
            if node2.left: q2.appendleft(node2.left)
            if node2.right: q2.appendleft(node2.right)

# DFS
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return
        if original == target:
            return cloned
        res = self.getTargetCopy(original.left,cloned.left,target)
        if res : return res
        res = self.getTargetCopy(original.right,cloned.right,target)
        if res : return res