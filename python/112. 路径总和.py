class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def count(node:TreeNode,sum:int) -> bool:
            if not node:
                return False
            if node.val == sum and not node.left and not node.right:
                return True
            leftCount = count(node.left,sum-node.val)
            if leftCount:
                return True
            rightCount = count(node.right,sum-node.val)
            if rightCount:
                return True
            return False

        if not root:
            return False

        if count(root,sum):return True
        # if self.hasPathSum(root.left,sum):return True
        # if self.hasPathSum(root.right,sum):return True
        return False