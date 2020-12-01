from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        from collections import defaultdict
        d = defaultdict(list)
        for i,j in edges:
            d[j].append(i)
        for k,v in d.items():
            while v[-1] != 0:
                v.extend(d[v[-1]])
        s = set()
        for i,v in enumerate(hasApple):
            if v:
                if len(d[i])>0:
                    tmp = str(i) + '-' +str(d[i][0])
                    s.add(tmp)
                    x = 1
                    while x < len(d[i]):
                        h = str(d[i][x-1]) + '-' + str(d[i][x])
                        s.add(h)
                        x+=1

        for i in s:
            print(s)
        return len(s)*2



s = Solution()
n = 4
edges = [[0,2],[0,3],[1,2]]
hasApple = [False,True,False,False]
print(s.minTime(n,edges,hasApple))
