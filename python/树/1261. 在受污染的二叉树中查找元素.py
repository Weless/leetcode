class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FindElements:

    def __init__(self, root: TreeNode):
        self.res = []
        self.dfs(root, 0)
        self.root = root

    def find(self, target: int) -> bool:
        return target in self.res

    def dfs(self, root, v):
        if not root: return
        root.val = v
        self.res.append(root.val)
        if root.left:
            self.dfs(root.left, 2 * root.val + 1)
        if root.right:
            self.dfs(root.right, 2 * root.val + 2)