class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from typing import List

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(root):
            if root:
                res.append(root.val)
                for node in root.children:
                    dfs(node)
        dfs(root)
        return res

# 迭代
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                for node in node.children[::-1]:
                    stack.append(node)
        return res