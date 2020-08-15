class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def dfs(root,v):
            if not root:
                return v
            left = dfs(root.left,v)
            right = dfs(root.right,v)
            v += root.val
        left = dfs(root.left,0)
        right = dfs(root.right,0)
        return abs(left-right)