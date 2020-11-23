class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root: return 1
            return 1 + max(dfs(root.left),dfs(root.right))
        left,right = dfs(root.left),dfs(root.right)
        if left == right:
            return root
        elif left > right:
            return self.subtreeWithAllDeepest(root.left)
        else:
            return self.subtreeWithAllDeepest(root.right)