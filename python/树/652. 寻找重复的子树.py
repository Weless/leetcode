from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        from collections import defaultdict
        d = defaultdict(int)
        res = []
        def dfs(root):
            if not root: return "#"
            left = dfs(root.left)
            right = dfs(root.right)
            subTree = left + ',' + right + ',' + str(root.val)
            d[subTree] += 1
            if d[subTree] == 2:
                res.append(root)
            return subTree
        dfs(root)
        return res