# 思路：
'''
1.一颗树只有一个节点,它的深度是1;
2.二叉树的根节点只有左子树而没有右子树,那么可以判断,二叉树的深度应该是其左子树的深度加1;
3.二叉树的根节点只有右子树而没有左子树,那么可以判断,那么二叉树的深度应该是其右树的深度加1;
4.二叉树的根节点既有右子树又有左子树,那么可以判断,那么二叉树的深度应该是其左右子树的深度较大值加1。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        depth = 1
        if root.left and not root.right:
            depth += self.maxDepth(root.left)
        elif not root.left and root.right:
            depth += self.maxDepth(root.right)
        elif root.left and root.right:
            depth += max(self.maxDepth(root.left),self.maxDepth(root.right))
        return depth

# 后序遍历
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# 层次遍历/广度优先（BFS）
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue, res = [root], 0
        while queue:
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
            res += 1
        return res

