class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left
        return root

# 迭代

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left,node.right = node.right,node.left
                stack.append(node.left)
                stack.append(node.right)
        return root