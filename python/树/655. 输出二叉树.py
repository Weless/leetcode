from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        m,n = 0,0
        def dfs(root):
            if not root:return 0
            left = dfs(root.left)
            right = dfs(root.right)
            return max(left,right) + 1
        m = dfs(root)
        n = 2**m-1
        res = [['' for _ in range(n)] for _ in range(m)]
        def draw(root,i,l,r):
            if not root: return
            mid = (l + r)//2
            res[i][mid] = str(root.val)
            draw(root.left,i+1,l,mid)
            draw(root.right,i+1,mid+1,r)
        draw(root,0,0,len(res[0]))
        return res