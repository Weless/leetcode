from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root):
            if not root:
                return
            if not root.left and root.right:
                res.append(root.right.val)
            elif not root.right and root.left:
                res.append(root.left.val)
            dfs(root.left)
            dfs(root.right)
        return res
