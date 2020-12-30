class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res = 0
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left + right <= distance:
                self.res += 1
            if not root.left and not root.right:
                return 1
            return min(left,right)+1
        dfs(root)
        return self.res
