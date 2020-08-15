class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        from collections import deque
        queue = deque()
        queue.append(root)
        res = 0
        while queue:
            node = queue.popleft()
            if node.left:
                if not node.left.left and not node.left.right:
                    res += node.left.val
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
