class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        self.pre = self.ans = TreeNode(-1)
        def dfs(root):
            if not root: return
            dfs(root.left)

            root.left = None
            self.pre.right = root
            self.pre = root

            dfs(root.right)
        dfs(root)
        return self.ans.right