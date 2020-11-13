from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        from collections import defaultdict,deque
        d = defaultdict(list)
        q = deque()
        q.appendleft((root,0,0))
        while q:
            tmp = []
            for _ in range(len(q)):
                node,x,y = q.pop()
                if x in tmp:
                    a = d[x].pop()
                    b = node.val
                    if a < b:
                        d[x].append(a)
                        d[x].append(b)
                    else:
                        d[x].append(b)
                        d[x].append(a)
                tmp.append(x)
                d[x].append(node.val)

                if node.left: q.appendleft((node.left,x-1,y-1))
                if node.right: q.appendleft((node.right,x+1,y-1))

        res = []
        for i in sorted(d):
            res.append(d[i])
        return res
