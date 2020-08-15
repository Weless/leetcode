class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        from collections import deque
        queue = deque()
        queue.append(root)
        _max = float('-inf')
        _max_level = 1
        level = 0
        while queue:
            tmp = 0
            level +=1
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if tmp > _max:
                _max = tmp
                _max_level = level
        return level

