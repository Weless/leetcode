class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        def dfs(root,n):
            if not root: return
            if n+1 == d:
                if root.left:
                    node = TreeNode(1)
                    node.left = root.left
                    root.left = node
                else:
                    node = TreeNode(v)
                    root.left = node
                if root.right:
                    node = TreeNode(v)
                    node.right = root.right
                    root.right = node
                else:
                    node = TreeNode(v)
                    root.right = node
            dfs(root.left,n+1)
            dfs(root.right,n+1)
        dfs(root,1)
        return root
