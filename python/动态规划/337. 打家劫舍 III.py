class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 暴力 超时

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        money = root.val
        if root.left:
            money += (self.rob(root.left.left)+ self.rob(root.left.right))
        if root.right:
            money += (self.rob(root.right.left)+self.rob(root.right.right))
        return max(money,self.rob(root.left)+self.rob(root.right))

# dict 超时

class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(root,tmp):
            if not root:
                return 0
            if root in tmp:
                tmp.get(root)
            money = root.val
            if root.left:
                money += (self.rob(root.left.left) + self.rob(root.left.right))
            if root.right:
                money += (self.rob(root.right.left) + self.rob(root.right.right))
            res = max(money, self.rob(root.left) + self.rob(root.right))
            tmp[root] = res
            return res
        tmp = dict()
        return helper(root,tmp)


# 当前节点选择不偷：当前节点能偷到的最大钱数 = 左孩子能偷到的钱 + 右孩子能偷到的钱
# 当前节点选择偷：当前节点能偷到的最大钱数 = 左孩子选择自己不偷时能得到的钱 + 右孩子选择不偷时能得到的钱 + 当前节点的钱数
# 每个节点设置为[不偷，偷]
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return [0,0]
            left = helper(root.left)
            right = helper(root.right)

            skipValue = max(left[0],left[1]) + max(right[0],right[1]) # 当前节点不偷
            robValue = left[0] + right[0] + root.val # 当前节点偷
            return [skipValue,robValue]
        res = helper(root)
        return max(res)