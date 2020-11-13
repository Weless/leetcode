class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def dfs(root):
            if not root: return ""
            left = dfs(root.left)
            right = dfs(root.right)
            return str(root.val)+","+left+","+right
        return dfs(root)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        alist = data.split(',')
        