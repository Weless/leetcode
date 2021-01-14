class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        from collections import deque
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                if i == l -1 :
                    res.append(node.val)
        return res


# DFS
class Solution:
    res = []
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.dfs(root,0)
        return self.res
    def dfs(self,root:TreeNode,depth):
        if not root:
            return
        if depth == len(self.res):
            self.res.append(root.val)
        depth+=1
        self.dfs(root.right,depth)
        self.dfs(root.left,depth)