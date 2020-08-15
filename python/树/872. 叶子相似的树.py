class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root,res):
            if root:
                if not root.left and not root.right:
                    res.append(root.val)
                dfs(root.left,res)
                dfs(root.right,res)
        res1,res2 =[],[]
        dfs(root1,res1)
        dfs(root2,res2)
        return True if res1 == res2 else False

# 官网解

class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))


