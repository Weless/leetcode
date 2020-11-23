from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root: return []
        from collections import defaultdict
        d = defaultdict(int)
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            sum = left + right + root.val
            d[sum] +=1
            return sum
        dfs(root)
        tmp = sorted(d.items(),key=lambda x:x[1],reverse=True)
        return [k for k,v in tmp if v == tmp[0][1]]