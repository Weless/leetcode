class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        self.pre = None
        def dfs(root):
            if not root:return
            if root.val == target and not root.left and not root.right:
                if self.pre.left and self.pre.left.val == root.val: self.pre.left = None
                if self.pre.right and self.pre.right.val == root.val: self.pre.right = None
                return
            self.pre = root
            dfs(root.left)
            dfs(root.right)

        def dfs2(root):
            if not root: return False
            if root.val == target:
                return True
            return dfs(root.left) or dfs(root.right)
        while dfs2(root):
            dfs(root)
        return root