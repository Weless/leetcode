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
            return left + ',' + right + ',' + str(root.val)
        return dfs(root)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = [int(x) for x in data.split(',')]
        def helper(lower = float('-inf'), upper = float('+inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return
            val = data.pop()
            root = TreeNode(val)
            root.left = helper(lower,val)
            root.right = helper(val,upper)
            return root
        return helper()