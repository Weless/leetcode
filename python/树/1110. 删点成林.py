from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        s = set(to_delete)
        res = []
        def dfs(root):
            if not root: return 
            cur = root.val
            if cur in s:
                if root.left:
                    if not root.left.val in s:
                        res.append(root.left)
                    dfs(root.left)
                if root.right:
                    if not root.right.val in s:
                        res.append(root.right)
                    dfs(root.right)
                return 
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            return root
        dfs(root)
        if root and not root.val in s:
            res.append(root)
        return res


