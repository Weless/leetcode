class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        res = []
        def dfs(root,path):
            if not root: return
            if not root.left and not root.right:
                s = "".join(map(chr,path))
                res.append(s)
            path.append(root.val)
            dfs(root.left)
            dfs(root.right)
            path.pop()
        dfs(root)
        print(res)