# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        from collections import deque
        queue = deque()
        queue.append(root)
        count = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.children:
                    for child in node.children:
                        queue.append(child)
            count+=1
        return count