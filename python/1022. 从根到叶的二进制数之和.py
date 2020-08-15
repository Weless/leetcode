class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(root,path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    res.append(path)
                dfs(root.left,path)
                dfs(root.right,path)
        res = []
        dfs(root,'')
        return sum([int(item,2) for item in res])