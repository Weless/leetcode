class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(root,v):
            if not root: return 0
            if v == 0:
                return 1
            left = dfs(root.left,v-root.val)
            right = dfs(root.left,v-root.val)
            return left + right
        if not root:
            return 0
        s = dfs(root,sum-root.val)
        print(s)