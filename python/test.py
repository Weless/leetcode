from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        q = deque()
        q.appendleft(root)
        l = 0
        res = []
        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.pop()
                tmp.append(node.val)
                if node.left: q.appendleft(node.left)
                if node.right: q.appendleft(node.right)
            if l % 2 == 0:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            l+=1
        return res


s = Solution()
m = 3
n = 2
print(s.uniquePaths(3,2))






