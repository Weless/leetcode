class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(root,s):
            if not root:
                return
            if not root.left and not root.right:
                s += str(root.val)
                return res.append(s)
            if root.left:
                dfs(root.left,s+str(root.val)+'->')
            if root.right:
                dfs(root.right,s+str(root.val)+'->')
        res = []
        dfs(root,'')
        return res


