class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        from collections import deque
        queue = deque()
        queue.appendleft(root)
        res = []
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.pop()
                if node.left: queue.appendleft(node.left)
                if node.right: queue.appendleft(node.right)
            res.append(tmp)
        return sum(res[-1])