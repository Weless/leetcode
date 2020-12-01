class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(root):
            if not root:
                return 0
            tmp = 0
            left = dfs(root.left)
            right = dfs(root.right)

            # 特殊情况，当root是最长路径的中间节点
            if root.left and root.right and root.left.val == root.val and root.right.val == root.val:
                # 这种情况只对于寻找最长路径长有帮助，对于搜索以root为路径起始点的最长路径没有帮助
                self.ans = max(self.ans, left + right + 2)
            # 从左右子树中选择最长的路径
            if root.left and root.left.val == root.val:
                tmp = left + 1
            if root.right and root.right.val == root.val:
                tmp = max(tmp, right + 1)
            self.ans = max(self.ans, tmp)
            return tmp
        dfs(root)
        return self.ans


