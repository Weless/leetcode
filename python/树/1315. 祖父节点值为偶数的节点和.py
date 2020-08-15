class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return
            if not root.val & 1:
                if root.left:
                    if root.left.left:
                        self.res += root.left.left.val
                    if root.left.right:
                        self.res += root.left.right.val
                if root.right:
                    if root.right.left:
                        self.res += root.right.left.val
                    if root.right.right:
                        self.res += root.right.right.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res