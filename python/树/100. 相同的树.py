class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def bfs(root:TreeNode):
            if not root:
                return []
            from collections import deque
            queue = deque()
            queue.append(root)
            res = []
            while queue:
                node = queue.pop()
                if node:
                    res.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res.append(None)
            return res

        return bfs(p) == bfs(q)


# 递归
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)
