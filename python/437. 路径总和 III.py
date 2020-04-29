class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def count(node:TreeNode,sum:int) -> int:
            if not node:
                return 0
            isMe = 1 if node.val == sum else 0
            leftCount = count(node.left,sum-node.val)
            rightCount = count(node.right,sum-node.val)
            return isMe + leftCount + rightCount

        if not root:
            return 0

        return count(root,sum) + self.pathSum(root.left,sum) + self.pathSum(root.right,sum)