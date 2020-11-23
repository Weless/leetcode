class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        from collections import deque
        q = deque()
        q.appendleft(root)
        c = 0
        while q:
            node = q.pop()
            c += 1
            if node.left: q.appendleft(node.left)
            if node.right: q.appendleft(node.right)
        return c