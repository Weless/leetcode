class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res = []
        def dfs(root):
            if not root: return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        res.sort()
        ans = float('+inf')
        for i in range(1,len(res)):
            ans = min(res[i] - res[i-1],ans)
        return ans

# 中序遍历
class Solution(object):
    def minDiffInBST(self, root):
        def dfs(node):
            if node:
                dfs(node.left)
                self.ans = min(self.ans, node.val - self.prev)
                self.prev = node.val
                dfs(node.right)

        self.prev = float('-inf')
        self.ans = float('inf')
        dfs(root)
        return self.ans

