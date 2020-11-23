class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
from typing import List
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
                if node.children:
                    for child in node.children:
                        queue.append(child)
            res.append(tmp)
        return res