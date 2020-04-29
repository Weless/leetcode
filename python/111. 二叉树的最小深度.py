class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 1
        from collections import deque
        queue = deque()
        queue.append(root)
        level = 1
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    return level
                if node.left: queue.append(node.left)
                if node.right:queue.append(node.right)
            level+=1
