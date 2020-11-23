class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root: return 0
            return 1+max(dfs(root.left),dfs(root.right))
        left = dfs(root.left)
        right = dfs(root.right)
        if left == right:
            return root
        elif left > right:
            return root.left
        else:
            return root.right
