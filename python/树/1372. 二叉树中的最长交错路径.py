from functools import lru_cache
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    @lru_cache(None)
    def dfs(self, root, dir):
        if not root:
            return 0
        if dir == -1:
            return int(root.left != None) + self.dfs(root.left, dir * -1)
        return int(root.right != None) + self.dfs(root.right, dir * -1)

    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.dfs(root, 1), self.dfs(root, -1), self.longestZigZag(root.left), self.longestZigZag(root.right))