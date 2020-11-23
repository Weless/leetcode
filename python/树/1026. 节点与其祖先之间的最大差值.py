class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 只要保留当前路径上遇到的最大值和最小值即可
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.result = 0
        def dfs(root,max,min):
            if not root:return
            val = root.val
            if val < min:
                min = val
            if val > max:
                max = val
            if max - min > self.result:
                self.result = max - min
            dfs(root.left,max,min)
            dfs(root.right,max,min)
        dfs(root,root.val,root.val)
        return self.result


