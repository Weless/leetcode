class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        from collections import deque
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(sum(tmp)*1.0/len(tmp))
        return res


# dfs

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        import collections
        traverse = collections.defaultdict(list)
        def dfs(node, n):
            if node:
                traverse[n] += [node.val]
                dfs(node.left,n+1)
                dfs(node.right,n+1)
        dfs(root, 0)
        return [sum(vals)/len(vals) for vals in traverse.values()]
