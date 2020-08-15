class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
from typing import List
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(root):
            if root:
                if root.children:
                    for child in root.children:
                       dfs(child)
                res.append(root.val)
        dfs(root)
        return res


# 迭代

class Solution(object):
    def postorder(self, root):
        if not root:
            return []
        stack,output = [root],[]
        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
            for c in node.children:
                stack.append(c)
        return output[::-1]