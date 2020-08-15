class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = []
        def dfs(root):
            if not root:
                return
            if root.left:
                if root.val == root.left.val:
                    dfs(root.left)
                else:
                    res.append(root.left.val)
            if root.right:
                if root.val == root.right.val:
                    dfs(root.right)
                else:
                    res.append(root.right.val)
        dfs(root)
        return -1 if len(res) == 0 else min(res)