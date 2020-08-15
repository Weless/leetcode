class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return 0
            return 1 +  max(dfs(root.left),dfs(root.right))
        if not root:
            return False
        left = dfs(root.left)
        right = dfs(root.right)
        return True if abs(left-right) <=1 else False




