class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        res = []
        def dfs(root):
            if root:
                if root.val not in res:
                    res.append(root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return True if len(res) == 1 else False