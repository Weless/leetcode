class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        i,j=0,1
        while j<len(res):
            
        return res
