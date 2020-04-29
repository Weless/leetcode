class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        def dfs(root:TreeNode,sum):
            if not root:
                return
            tmp.append(root.val)
            if not root.left and not root.right and root.val == sum:
                res.append(tmp[:])
            dfs(root.left,sum-root.val)
            dfs(root.right,sum-root.val)
            tmp.pop()

        tmp = []
        res = []
        dfs(root,sum)
        return res
