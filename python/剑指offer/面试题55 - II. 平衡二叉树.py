# 后序遍历 + 减枝
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def recur(root):
            if not root: return 0
            left = recur(root.left)
            if left == -1: return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return recur(root) != -1

# 先序遍历 + 深度

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root:TreeNode):
            if not root:
                return 0
            return max(depth(root.left),depth(root.right))+1
        if not root:
            return True
        left_depth = depth(root.left)
        right_depth = depth(root.right)
        return abs(left_depth-right_depth)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)