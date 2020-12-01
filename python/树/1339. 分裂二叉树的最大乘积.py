class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    res = set()
    def maxProduct(self, root: TreeNode) -> int:
        num = self.get_sum(root)
        ans = 0
        for i in self.res:
            ans = max(ans,i*(num-i))
        ans %= 10**9+7
        return ans

    def get_sum(self,root):
        if not root: return 0
        val = root.val + self.get_sum(root.left) + self.get_sum(root.right)
        self.res.add(val)
        return val
